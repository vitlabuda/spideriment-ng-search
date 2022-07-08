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
from typing import Any
import abc
from spideriment_ng_search.config.ScoringConfiguration import ScoringConfiguration
from spideriment_ng_search.containers.search.SearchQuery import SearchQuery
from spideriment_ng_search.containers.search.DocumentSearchResults import DocumentSearchResults
from spideriment_ng_search.containers.search.ImageSearchResults import ImageSearchResults
from spideriment_ng_search.containers.document_info.DocumentInfo import DocumentInfo
from spideriment_ng_search.databases.drivers.DatabaseDriverInfo import DatabaseDriverInfo


class DatabaseDriverIface(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def get_database_driver_info(cls) -> DatabaseDriverInfo:
        raise NotImplementedError(cls.get_database_driver_info.__qualname__)

    @classmethod
    @abc.abstractmethod
    def create_instance(cls, driver_options: Any) -> DatabaseDriverIface:
        """
        :raises DatabaseInstanceCreationFailureExc
        """

        raise NotImplementedError(cls.create_instance.__qualname__)

    @abc.abstractmethod
    def destroy_instance(self) -> None:
        """
        :raises DatabaseInstanceDestructionFailureExc
        """

        raise NotImplementedError(self.__class__.destroy_instance.__qualname__)

    @abc.abstractmethod
    def perform_document_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> DocumentSearchResults:
        """
        The returned search result sequence MUST be ordered by the results' scores!
        The whole search & scoring process is done via the database module due to possible optimizations - it is not
         necessary for the databases to send unnecessary data to the application.

        :raises DatabaseUseFailureExc
        """

        raise NotImplementedError(self.__class__.perform_document_search.__qualname__)

    @abc.abstractmethod
    def perform_image_search(self, search_query: SearchQuery, scoring_config: ScoringConfiguration) -> ImageSearchResults:
        """
        The returned search result sequence MUST be ordered by the results' scores!
        The whole search & scoring process is done via the database module due to possible optimizations - it is not
         necessary for the databases to send unnecessary data to the application.

        :raises DatabaseUseFailureExc
        """

        raise NotImplementedError(self.__class__.perform_image_search.__qualname__)

    @abc.abstractmethod
    def obtain_document_info(self, url: str) -> DocumentInfo:
        raise NotImplementedError(self.__class__.obtain_document_info.__qualname__)
