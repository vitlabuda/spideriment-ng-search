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


from typing import Final, Sequence, Any
import datetime
import pymysql
from spideriment_ng_search.containers.document_info.DocumentInfo import DocumentInfo
from spideriment_ng_search.containers.document_info.ContentSnippet import ContentSnippet
from spideriment_ng_search.containers.document_info.Link import Link
from spideriment_ng_search.containers.document_info.Image import Image
from spideriment_ng_search.databases.drivers.exc.DatabaseUseFailureExc import DatabaseUseFailureExc
from spideriment_ng_search.databases.drivers.mysql._facade._MySQLFacadedClassBase import _MySQLFacadedClassBase


class DocumentInfoObtainer(_MySQLFacadedClassBase):
    _OBTAIN_BASIC_DOCUMENT_INFO_SELECT_QUERY: Final[str] = """
        SELECT
            `documents`.`document_id` AS `id`,
            `links`.`link_href_url` AS `url`,
            `documents`.`document_title` AS `title`,
            `documents`.`document_description` AS `description`,
            `filetypes`.`filetype_name` AS `filetype`,
            `languages`.`language_code` AS `language`,
            `authors`.`author_name` AS `author`,
            `documents`.`document_crawled_at` AS `crawled_at`
        FROM `documents`
        INNER JOIN `links` ON `links`.`link_id` = `documents`.`document_final_link_id`
        INNER JOIN `filetypes` ON `filetypes`.`filetype_id` = `documents`.`document_filetype_id`
        INNER JOIN `languages` ON `languages`.`language_id` = `documents`.`document_language_id`
        INNER JOIN `authors` ON `authors`.`author_id` = `documents`.`document_author_id`
        WHERE `links`.`link_href_url` = %(url)s;
    """

    _OBTAIN_DOCUMENT_KEYWORDS_SELECT_QUERY: Final[str] = """
        SELECT
            `keywords`.`keyword_text` AS `keyword`
        FROM `keywords`
        INNER JOIN `document_keyword_pairs` ON `document_keyword_pairs`.`document_keyword_pair_keyword_id` = `keywords`.`keyword_id`
        WHERE `document_keyword_pairs`.`document_keyword_pair_document_id` = %(document_id)s
        ORDER BY `keywords`.`keyword_id` ASC;
    """

    _OBTAIN_DOCUMENT_CONTENT_SNIPPETS_SELECT_QUERY: Final[str] = """
        SELECT
            `content_snippets`.`content_snippet_type` AS `type`,
            `content_snippets`.`content_snippet_text` AS `text`
        FROM `content_snippets`
        WHERE `content_snippets`.`content_snippet_document_id` = %(document_id)s
        ORDER BY `content_snippets`.`content_snippet_type` ASC, `content_snippets`.`content_snippet_id` ASC;
    """

    _OBTAIN_DOCUMENT_LINKS_SELECT_QUERY: Final[str] = """
        SELECT 
            `links`.`link_href_url` AS `url`,
            `document_link_pairs`.`document_link_pair_link_text` AS `text`
        FROM `links`
        INNER JOIN `document_link_pairs` ON `document_link_pairs`.`document_link_pair_link_id` = `links`.`link_id`
        WHERE `document_link_pairs`.`document_link_pair_document_id` = %(document_id)s
        ORDER BY `links`.`link_id` ASC;
    """

    _OBTAIN_DOCUMENT_IMAGES_SELECT_QUERY: Final[str] = """
        SELECT
            `images`.`image_src_url` AS `url`,
            `document_image_pairs`.`document_image_pair_image_alt_text` AS `alt_text`,
            `document_image_pairs`.`document_image_pair_image_title_text` AS `title_text`
        FROM `images`
        INNER JOIN `document_image_pairs` ON `document_image_pairs`.`document_image_pair_image_id` = `images`.`image_id`
        WHERE `document_image_pairs`.`document_image_pair_document_id` = %(document_id)s
        ORDER BY `images`.`image_id` ASC;
    """

    _MYSQL_ERROR_SURROGATE_MESSAGE: Final[str] = "Failed to obtain the requested document info using the server's configured database!"

    def obtain_document_info(self, url: str) -> DocumentInfo:
        basic_document_info = self._obtain_basic_document_info(url)
        document_id = int(basic_document_info["id"])
        assert isinstance(basic_document_info["crawled_at"], datetime.datetime)

        keywords = self._obtain_objects_from_document(self.__class__._OBTAIN_DOCUMENT_KEYWORDS_SELECT_QUERY, document_id)
        content_snippets = self._obtain_objects_from_document(self.__class__._OBTAIN_DOCUMENT_CONTENT_SNIPPETS_SELECT_QUERY, document_id)
        links = self._obtain_objects_from_document(self.__class__._OBTAIN_DOCUMENT_LINKS_SELECT_QUERY, document_id)
        images = self._obtain_objects_from_document(self.__class__._OBTAIN_DOCUMENT_IMAGES_SELECT_QUERY, document_id)

        return DocumentInfo(
            url=str(basic_document_info["url"]),
            title=str(basic_document_info["title"]),
            description=str(basic_document_info["description"]),
            filetype=str(basic_document_info["filetype"]),
            language=str(basic_document_info["language"]),
            author=str(basic_document_info["author"]),
            keywords=tuple(str(keyword["keyword"]) for keyword in keywords),
            content_snippets=tuple(ContentSnippet(
                type_=str(content_snippet["type"]),
                text=str(content_snippet["text"])
            ) for content_snippet in content_snippets),
            links=tuple(Link(
                url=str(link["url"]),
                text=str(link["text"])
            ) for link in links),
            images=tuple(Image(
                url=str(image["url"]),
                alt_text=str(image["alt_text"]),
                title_text=str(image["title_text"])
            ) for image in images),
            crawled_at=basic_document_info["crawled_at"].replace()
        )

    def _obtain_basic_document_info(self, url: str) -> dict[str, Any]:
        try:
            with self._mysql_connection.cursor() as cursor:
                cursor.execute(
                    query=self.__class__._OBTAIN_BASIC_DOCUMENT_INFO_SELECT_QUERY,
                    args={"url": url}
                )
                results = cursor.fetchall()
        except pymysql.Error:
            raise DatabaseUseFailureExc(
                db_driver_name=self._db_driver_name,
                user_readable_error_message=self.__class__._MYSQL_ERROR_SURROGATE_MESSAGE
            )

        if len(results) != 1:
            raise DatabaseUseFailureExc(
                db_driver_name=self._db_driver_name,
                user_readable_error_message=f"A document with the URL of {repr(url)} is not present in the database!"
            )

        return results[0]  # noqa

    def _obtain_objects_from_document(self, select_query: str, document_id: int) -> Sequence[dict[str, Any]]:
        try:
            with self._mysql_connection.cursor() as cursor:
                cursor.execute(
                    query=select_query,
                    args={"document_id": document_id}
                )
                results = cursor.fetchall()
        except pymysql.Error:
            raise DatabaseUseFailureExc(
                db_driver_name=self._db_driver_name,
                user_readable_error_message=self.__class__._MYSQL_ERROR_SURROGATE_MESSAGE
            )

        return results  # noqa
