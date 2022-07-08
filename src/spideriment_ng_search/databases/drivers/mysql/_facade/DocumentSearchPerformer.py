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
from spideriment_ng_search.containers.search.DocumentSearchResult import DocumentSearchResult
from spideriment_ng_search.containers.search.DocumentSearchResults import DocumentSearchResults
from spideriment_ng_search.databases.drivers.exc.DatabaseUseFailureExc import DatabaseUseFailureExc
from spideriment_ng_search.databases.drivers.mysql._facade._MySQLFacadedClassBase import _MySQLFacadedClassBase


class DocumentSearchPerformer(_MySQLFacadedClassBase):
    # This query looks TERRIBLE, but it seems that there are no other ways to do this (at least in a single query)...
    _PERFORM_DOCUMENT_SEARCH_SELECT_QUERY: Final[str] = """
        SELECT 
            `documents`.`document_title` AS `title`,
            IFNULL(
                NULLIF(
                    `documents`.`document_description`, 
                    ''
                ),
                IFNULL(
                    (
                        SELECT `content_snippets`.`content_snippet_text` 
                        FROM `content_snippets`
                        WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        ORDER BY CHAR_LENGTH(`content_snippets`.`content_snippet_text`) DESC
                        LIMIT 1
                    ),
                    ''
                )
            ) AS `snippet`,
            `links`.`link_href_url` AS `url`,
            (
                (
                    MATCH(`documents`.`document_title`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE) * %(title_score_multiplier)s
                ) +
                (
                    MATCH(`documents`.`document_description`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE) * %(description_score_multiplier)s
                ) + 
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(heading_1_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'heading_1'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(heading_2_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'heading_2'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(heading_3_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'heading_3'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(heading_4_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'heading_4'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(heading_5_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'heading_5'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(emphasized_text_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'emphasized_text'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(regular_text_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'regular_text'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(list_item_text_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'list_item_text'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(uncategorized_text_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'uncategorized_text'
                ) +
                (
                    SELECT IFNULL(SUM(MATCH(`content_snippets`.`content_snippet_text`) AGAINST(%(search_query)s IN NATURAL LANGUAGE MODE)), 0) * %(fallback_text_score_multiplier)s
                    FROM `content_snippets`
                    WHERE `content_snippets`.`content_snippet_document_id` = `documents`.`document_id`
                        AND `content_snippets`.`content_snippet_type` = 'fallback_text'
                )
            ) AS `score`
        FROM `documents`
        INNER JOIN `links` ON `links`.`link_id` = `documents`.`document_final_link_id`
        HAVING `score` >= %(min_total_score)s
        ORDER BY `score` DESC
        LIMIT %(max_results)s;
    """

    _MYSQL_ERROR_SURROGATE_MESSAGE: Final[str] = "Failed to perform the requested document search using the server's configured database!"

    def perform_document_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> DocumentSearchResults:
        try:
            with self._mysql_connection.cursor() as cursor:
                cursor.execute(
                    query=self.__class__._PERFORM_DOCUMENT_SEARCH_SELECT_QUERY,
                    args={
                        "search_query": search_query.search_query,
                        "title_score_multiplier": scoring_config.title_score_multiplier,
                        "description_score_multiplier": scoring_config.description_score_multiplier,
                        "heading_1_score_multiplier": scoring_config.heading_1_score_multiplier,
                        "heading_2_score_multiplier": scoring_config.heading_2_score_multiplier,
                        "heading_3_score_multiplier": scoring_config.heading_3_score_multiplier,
                        "heading_4_score_multiplier": scoring_config.heading_4_score_multiplier,
                        "heading_5_score_multiplier": scoring_config.heading_5_score_multiplier,
                        "emphasized_text_score_multiplier": scoring_config.emphasized_text_score_multiplier,
                        "regular_text_score_multiplier": scoring_config.regular_text_score_multiplier,
                        "list_item_text_score_multiplier": scoring_config.list_item_text_score_multiplier,
                        "uncategorized_text_score_multiplier": scoring_config.uncategorized_text_score_multiplier,
                        "fallback_text_score_multiplier": scoring_config.fallback_text_score_multiplier,
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

        return DocumentSearchResults(
            search_results=tuple(DocumentSearchResult(
                url=str(result["url"]),  # noqa
                title=str(result["title"]),  # noqa
                snippet=str(result["snippet"]),  # noqa
                score=float(result["score"])  # noqa
            ) for result in results)
        )
