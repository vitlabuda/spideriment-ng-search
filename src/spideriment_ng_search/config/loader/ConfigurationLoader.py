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
import os
import fcntl
import tomlkit
import tomlkit.exceptions
from datalidator.exc.DatalidatorExc import DatalidatorExc
from datalidator.blueprints.impl.ObjectBlueprint import ObjectBlueprint
from spideriment_ng_search.config.Configuration import Configuration
from spideriment_ng_search.config.GenericConfiguration import GenericConfiguration
from spideriment_ng_search.config.DatabaseConfiguration import DatabaseConfiguration
from spideriment_ng_search.config.ScoringConfiguration import ScoringConfiguration
from spideriment_ng_search.config.WebViewConfiguration import WebViewConfiguration
from spideriment_ng_search.config.loader._ConfigModel import _ConfigModel
from spideriment_ng_search.config.loader._GenericConfigModel import _GenericConfigModel
from spideriment_ng_search.config.loader._DatabaseConfigModel import _DatabaseConfigModel
from spideriment_ng_search.config.loader._ScoringConfigModel import _ScoringConfigModel
from spideriment_ng_search.config.loader._WebViewConfigModel import _WebViewConfigModel
from spideriment_ng_search.config.loader.exc.FailedToReadConfigFileExc import FailedToReadConfigFileExc
from spideriment_ng_search.config.loader.exc.FailedToParseConfigExc import FailedToParseConfigExc
from spideriment_ng_search.config.loader.exc.InvalidConfigContentsExc import InvalidConfigContentsExc
from spideriment_ng_search.databases.registry.DatabaseDriverRegistry import DatabaseDriverRegistry
from spideriment_ng_search.databases.registry.exc.DatabaseDriverNotFoundExc import DatabaseDriverNotFoundExc


class ConfigurationLoader:
    _CONFIG_BLUEPRINT: Final[ObjectBlueprint] = ObjectBlueprint(_ConfigModel)

    def load_config_from_toml_file(self, toml_file_path: str) -> Configuration:
        try:
            with open(toml_file_path) as toml_file:
                fcntl.flock(toml_file.fileno(), fcntl.LOCK_SH)
                try:
                    toml_string = toml_file.read()
                finally:
                    fcntl.flock(toml_file.fileno(), fcntl.LOCK_UN)
        except OSError as e:
            raise FailedToReadConfigFileExc(
                config_file_path=toml_file_path,
                working_directory=os.getcwd(),
                failure_reason=str(e)
            )

        return self.load_config_from_toml_string(toml_string)

    def load_config_from_toml_string(self, toml_string: str) -> Configuration:
        try:
            config_dict = tomlkit.loads(toml_string)
        except tomlkit.exceptions.TOMLKitError as e:
            raise FailedToParseConfigExc(str(e))

        return self.load_config_from_dict(config_dict)

    def load_config_from_dict(self, config_dict: dict) -> Configuration:
        try:
            config_model = self.__class__._CONFIG_BLUEPRINT.use(config_dict)
        except DatalidatorExc as e:
            raise InvalidConfigContentsExc(str(e))

        return self._load_config_from_model(config_model)  # noqa

    def _load_config_from_model(self, config_model: _ConfigModel) -> Configuration:
        return Configuration(
            generic_config=self._load_generic_config_from_model(config_model.generic),
            database_config=self._load_database_config_from_model(config_model.database),
            scoring_config=self._load_scoring_config_from_model(config_model.scoring),
            web_view_config=self._load_web_view_config_from_model(config_model.web_view)
        )

    def _load_generic_config_from_model(self, generic_config_model: _GenericConfigModel) -> GenericConfiguration:
        return GenericConfiguration(**vars(generic_config_model))

    def _load_database_config_from_model(self, database_config_model: _DatabaseConfigModel) -> DatabaseConfiguration:
        try:
            driver_class = DatabaseDriverRegistry.get_database_driver_by_name(database_config_model.driver)
        except DatabaseDriverNotFoundExc as e:
            raise InvalidConfigContentsExc(str(e))

        try:
            datalidated_options = driver_class.get_database_driver_info().configuration_blueprint.use(database_config_model.options)
        except DatalidatorExc as f:
            raise InvalidConfigContentsExc(str(f))

        return DatabaseConfiguration(
            driver_class=driver_class,
            datalidated_options=datalidated_options
        )

    def _load_scoring_config_from_model(self, scoring_config_model: _ScoringConfigModel) -> ScoringConfiguration:
        return ScoringConfiguration(**vars(scoring_config_model))

    def _load_web_view_config_from_model(self, web_view_config_model: _WebViewConfigModel) -> WebViewConfiguration:
        return WebViewConfiguration(**vars(web_view_config_model))
