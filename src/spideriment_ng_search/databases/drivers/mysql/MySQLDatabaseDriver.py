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


from __future__ import annotations
from typing import Final
import pymysql
import pymysql.cursors
from datalidator.blueprints.impl.ObjectBlueprint import ObjectBlueprint
from spideriment_ng_search.config.ScoringConfiguration import ScoringConfiguration
from spideriment_ng_search.containers.document_info.DocumentInfo import DocumentInfo
from spideriment_ng_search.containers.search.SearchQuery import SearchQuery
from spideriment_ng_search.containers.search.DocumentSearchResults import DocumentSearchResults
from spideriment_ng_search.containers.search.ImageSearchResults import ImageSearchResults
from spideriment_ng_search.databases.drivers.DatabaseDriverIface import DatabaseDriverIface
from spideriment_ng_search.databases.drivers.DatabaseDriverInfo import DatabaseDriverInfo
from spideriment_ng_search.databases.drivers.mysql._MySQLDatabaseDriverConfigModel import _MySQLDatabaseDriverConfigModel
from spideriment_ng_search.databases.drivers.mysql._facade.DocumentSearchPerformer import DocumentSearchPerformer  # noqa
from spideriment_ng_search.databases.drivers.mysql._facade.ImageSearchPerformer import ImageSearchPerformer  # noqa
from spideriment_ng_search.databases.drivers.mysql._facade.DocumentInfoObtainer import DocumentInfoObtainer  # noqa
from spideriment_ng_search.databases.drivers.exc.DatabaseInstanceCreationFailureExc import DatabaseInstanceCreationFailureExc
from spideriment_ng_search.databases.drivers.exc.DatabaseInstanceDestructionFailureExc import DatabaseInstanceDestructionFailureExc


class MySQLDatabaseDriver(DatabaseDriverIface):  # DP: Facade
    _DATABASE_DRIVER_NAME: Final[str] = "mysql"
    _DATABASE_DRIVER_INFO: Final[DatabaseDriverInfo] = DatabaseDriverInfo(
        name=_DATABASE_DRIVER_NAME,
        configuration_blueprint=ObjectBlueprint(_MySQLDatabaseDriverConfigModel)
    )

    _CHARACTER_SET: Final[str] = "utf8mb4"
    _COLLATION: Final[str] = "utf8mb4_general_ci"

    @classmethod
    def get_database_driver_info(cls) -> DatabaseDriverInfo:
        return cls._DATABASE_DRIVER_INFO

    def __init__(self, mysql_host: str, mysql_port: int, mysql_user: str, mysql_password: str, mysql_db: str):
        try:
            self._mysql_connection: Final[pymysql.Connection] = pymysql.connect(
                host=mysql_host,
                user=mysql_user,
                password=mysql_password,
                database=mysql_db,
                port=mysql_port,
                charset=self.__class__._CHARACTER_SET,
                autocommit=False,
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.Error:
            raise DatabaseInstanceCreationFailureExc(
                db_driver_name=self.__class__._DATABASE_DRIVER_NAME,
                user_readable_error_message="Failed to connect to the server's configured database!"
            )

        self._operational: bool = True

    @classmethod
    def create_instance(cls, driver_options: _MySQLDatabaseDriverConfigModel) -> DatabaseDriverIface:
        return cls(
            mysql_host=driver_options.mysql_host,
            mysql_port=driver_options.mysql_port,
            mysql_user=driver_options.mysql_user,
            mysql_password=driver_options.mysql_password,
            mysql_db=driver_options.mysql_db
        )

    def destroy_instance(self) -> None:
        assert self._operational
        self._operational = False

        try:
            self._mysql_connection.close()
        except pymysql.Error:
            raise DatabaseInstanceDestructionFailureExc(
                db_driver_name=self.__class__._DATABASE_DRIVER_NAME,
                user_readable_error_message="Failed to close an opened connection to the server's configured database!"
            )

    def perform_document_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> DocumentSearchResults:
        assert self._operational
        assert (search_query.max_results > 0)

        return DocumentSearchPerformer(self._mysql_connection, self.__class__._DATABASE_DRIVER_NAME).perform_document_search(search_query, scoring_config)

    def perform_image_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> ImageSearchResults:
        assert self._operational
        assert (search_query.max_results > 0)

        return ImageSearchPerformer(self._mysql_connection, self.__class__._DATABASE_DRIVER_NAME).perform_image_search(search_query, scoring_config)

    def obtain_document_info(self, url: str) -> DocumentInfo:
        assert self._operational

        return DocumentInfoObtainer(self._mysql_connection, self.__class__._DATABASE_DRIVER_NAME).obtain_document_info(url)
