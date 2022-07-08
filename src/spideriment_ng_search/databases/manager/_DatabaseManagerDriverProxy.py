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


from typing import Final, Any
from spideriment_ng_search.exc.ThisShouldNeverHappenError import ThisShouldNeverHappenError
from spideriment_ng_search.config.ScoringConfiguration import ScoringConfiguration
from spideriment_ng_search.containers.search.SearchQuery import SearchQuery
from spideriment_ng_search.containers.search.DocumentSearchResults import DocumentSearchResults
from spideriment_ng_search.containers.search.ImageSearchResults import ImageSearchResults
from spideriment_ng_search.containers.document_info.DocumentInfo import DocumentInfo
from spideriment_ng_search.databases.drivers.DatabaseDriverIface import DatabaseDriverIface
from spideriment_ng_search.databases.drivers.DatabaseDriverInfo import DatabaseDriverInfo


class _DatabaseManagerDriverProxy(DatabaseDriverIface):
    def __init__(self, database_driver_instance: DatabaseDriverIface):
        self._database_driver_instance: Final[DatabaseDriverIface] = database_driver_instance

    @classmethod
    def get_database_driver_info(cls) -> DatabaseDriverInfo:
        raise ThisShouldNeverHappenError(f"Illegal use of method {repr(cls.get_database_driver_info.__name__)}!")

    @classmethod
    def create_instance(cls, driver_options: Any) -> DatabaseDriverIface:
        raise ThisShouldNeverHappenError(f"Illegal use of method {repr(cls.create_instance.__name__)}!")

    def destroy_instance(self) -> None:
        raise ThisShouldNeverHappenError(f"Illegal use of method {repr(self.__class__.destroy_instance.__name__)}!")

    def perform_document_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> DocumentSearchResults:
        return self._database_driver_instance.perform_document_search(search_query, scoring_config)

    def perform_image_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> ImageSearchResults:
        return self._database_driver_instance.perform_image_search(search_query, scoring_config)

    def obtain_document_info(self, url: str) -> DocumentInfo:
        return self._database_driver_instance.obtain_document_info(url)
