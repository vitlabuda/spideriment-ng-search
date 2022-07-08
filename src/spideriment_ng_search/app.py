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


import os
import flask
from spideriment_ng_search.SpiderimentSearchConstants import SpiderimentSearchConstants
from spideriment_ng_search.config.loader.ConfigurationLoader import ConfigurationLoader
from spideriment_ng_search.di import DI_NS
from spideriment_ng_search.di.SpiderimentSearchDependencyProvider import SpiderimentSearchDependencyProvider
from spideriment_ng_search.databases.manager.DatabaseManager import DatabaseManager


# Configure the app
try:
    _config_file_path = os.environ[SpiderimentSearchConstants.CONFIG_FILE_PATH_ENVVAR].strip()
except KeyError:
    _config_file_path = SpiderimentSearchConstants.DEFAULT_CONFIG_FILE_PATH

_configuration = ConfigurationLoader().load_config_from_toml_file(_config_file_path)
_database_manager = DatabaseManager(_configuration.database_config)

DI_NS.set_dependency_provider(SpiderimentSearchDependencyProvider(
    configuration=_configuration,
    database_manager=_database_manager
))


# Initialize the app
app = flask.Flask(__name__)

from spideriment_ng_search.blueprint_web import blueprint_web
from spideriment_ng_search.blueprint_api import blueprint_api
app.register_blueprint(blueprint_web)
app.register_blueprint(blueprint_api)


@app.route("/", methods=("GET",))
def index():
    return flask.redirect(flask.url_for("blueprint_web.document_search"))


@app.route("/robots.txt", methods=("GET",))
def robots_txt():
    return blueprint_web.send_static_file("robots.txt")
