#!/bin/false

# Copyright (c) 2022 Vít Labuda. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
#     disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#     following disclaimer in the documentation and/or other materials provided with the distribution.
#  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#     products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from typing import Final
import pymysql
from spideriment_ng_search.config.ScoringConfiguration import ScoringConfiguration
from spideriment_ng_search.containers.search.SearchQuery import SearchQuery
from spideriment_ng_search.containers.search.ImageSearchResult import ImageSearchResult
from spideriment_ng_search.containers.search.ImageSearchResults import ImageSearchResults
from spideriment_ng_search.databases.drivers.exc.DatabaseUseFailureExc import DatabaseUseFailureExc
from spideriment_ng_search.databases.drivers.mysql._facade._MySQLFacadedClassBase import _MySQLFacadedClassBase


class ImageSearchPerformer(_MySQLFacadedClassBase):
    _PERFORM_IMAGE_SEARCH_SELECT_QUERY: Final[str] = """
        SELECT 
            `images`.`image_src_url` AS `url`,
            IFNULL(
                NULLIF(
                    (
                        SELECT `document_image_pairs`.`document_image_pair_image_title_text`
                        FROM `document_image_pairs`
                        WHERE `document_image_pairs`.`document_image_pair_image_id` = `images`.`image_id`
                        ORDER BY CHAR_LENGTH(`document_image_pairs`.`document_image_pair_image_title_text`) DESC
                        LIMIT 1
                    ),
                    ''
                ),
                IFNULL(
                    (
                        SELECT `document_image_pairs`.`document_image_pair_image_alt_text`
                        FROM `document_image_pairs`
                        WHERE `document_image_pairs`.`document_image_pair_image_id` = `images`.`image_id`
                        ORDER BY CHAR_LENGTH(`document_image_pairs`.`document_image_pair_image_alt_text`) DESC
                        LIMIT 1
                    ),
                    ''
                )
            ) AS `description`,
            (
                SELECT
                    (
                        (
                            IFNULL(SUM(MATCH(`document_image_pairs`.`document_image_pair_image_alt_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(image_alt_text_score_multiplier)s
                        ) +
                        (
                            IFNULL(SUM(MATCH(`document_image_pairs`.`document_image_pair_image_title_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(image_title_text_score_multiplier)s
                        )
                    )
                FROM `document_image_pairs`
                WHERE `document_image_pairs`.`document_image_pair_image_id` = `images`.`image_id`
            ) AS `score`
        FROM `images`
        HAVING `score` >= %(min_total_score)s
        ORDER BY `score` DESC
        LIMIT %(max_results)s;
    """

    _MYSQL_ERROR_SURROGATE_MESSAGE: Final[str] = "Failed to perform the requested image search using the server's configured database!"

    def perform_image_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> ImageSearchResults:
        try:
            with self._mysql_connection.cursor() as cursor:
                cursor.execute(
                    query=self.__class__._PERFORM_IMAGE_SEARCH_SELECT_QUERY,
                    args={
                        "search_query": search_query.search_query,
                        "image_alt_text_score_multiplier": scoring_config.image_alt_text_score_multiplier,
                        "image_title_text_score_multiplier": scoring_config.image_title_text_score_multiplier,
                        "min_total_score": scoring_config.min_total_score,
                        "max_results": search_query.max_results
                    }
                )
                results = cursor.fetchall()
        except pymysql.Error:
            raise DatabaseUseFailureExc(
                db_driver_name=self._db_driver_name,
                user_readable_error_message=self.__class__._MYSQL_ERROR_SURROGATE_MESSAGE
            )

        return ImageSearchResults(
            search_results=tuple(ImageSearchResult(
                url=str(result["url"]),  # noqa
                description=str(result["description"]),  # noqa
                score=float(result["score"])  # noqa
            ) for result in results)
        )
