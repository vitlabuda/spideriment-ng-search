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


import flask
from spideriment_ng_search.SpiderimentSearchConstants import SpiderimentSearchConstants
from spideriment_ng_search.config.Configuration import Configuration
from spideriment_ng_search.containers.search.SearchQuery import SearchQuery
from spideriment_ng_search.containers.search.DocumentSearchResults import DocumentSearchResults
from spideriment_ng_search.containers.search.ImageSearchResults import ImageSearchResults
from spideriment_ng_search.containers.document_info.DocumentInfo import DocumentInfo
from spideriment_ng_search.di import DI_NS
from spideriment_ng_search.mvc.Controller import Controller
from spideriment_ng_search.mvc.input_parsers.InputDictSource import InputDictSource
from spideriment_ng_search.mvc.input_parsers.impl.SearchQueryInputParser import SearchQueryInputParser
from spideriment_ng_search.mvc.input_parsers.impl.URLInputParser import URLInputParser
from spideriment_ng_search.mvc.models.impl.DocumentSearchModel import DocumentSearchModel
from spideriment_ng_search.mvc.models.impl.ImageSearchModel import ImageSearchModel
from spideriment_ng_search.mvc.models.impl.DocumentInfoModel import DocumentInfoModel
from spideriment_ng_search.mvc.views.constants.WebTitleTexts import WebTitleTexts
from spideriment_ng_search.mvc.views.impl.WebDocumentSearchView import WebDocumentSearchView
from spideriment_ng_search.mvc.views.impl.WebImageSearchView import WebImageSearchView
from spideriment_ng_search.mvc.views.impl.WebDocumentInfoView import WebDocumentInfoView


blueprint_web = flask.Blueprint(
    "blueprint_web",
    __name__,
    static_folder="web_static",
    static_url_path="static",
    template_folder="web_templates",
    url_prefix="/web"
)


@blueprint_web.context_processor
@DI_NS.inject_dependencies("configuration")
def blueprint_web_context_processor(configuration: Configuration):
    return {
        "G_program_version": SpiderimentSearchConstants.PROGRAM_VERSION,
        "G_instance_name": configuration.generic_config.instance_name,
        "G_web_title_texts": WebTitleTexts,
        "G_web_view_config": configuration.web_view_config
    }


@blueprint_web.route("/document-search", methods=("GET",))
def document_search():
    input_parser = SearchQueryInputParser(input_dict_source=InputDictSource.GET_PARAMS)
    model = DocumentSearchModel()
    view = WebDocumentSearchView()

    return Controller[SearchQuery, DocumentSearchResults](
        input_parser=input_parser,
        model=model,
        success_view=view,
        error_view=view
    ).use_controller(flask.request)


@blueprint_web.route("/image-search", methods=("GET",))
def image_search():
    input_parser = SearchQueryInputParser(input_dict_source=InputDictSource.GET_PARAMS)
    model = ImageSearchModel()
    view = WebImageSearchView()

    return Controller[SearchQuery, ImageSearchResults](
        input_parser=input_parser,
        model=model,
        success_view=view,
        error_view=view
    ).use_controller(flask.request)


@blueprint_web.route("/document-info", methods=("GET",))
def document_info():
    input_parser = URLInputParser(input_dict_source=InputDictSource.GET_PARAMS)
    model = DocumentInfoModel()
    view = WebDocumentInfoView()

    return Controller[str, DocumentInfo](
        input_parser=input_parser,
        model=model,
        success_view=view,
        error_view=view
    ).use_controller(flask.request)
