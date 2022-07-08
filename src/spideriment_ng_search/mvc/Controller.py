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


from typing import Final, Generic, TypeVar, Optional
import flask
from spideriment_ng_search.mvc.input_parsers.InputParserIface import InputParserIface
from spideriment_ng_search.mvc.input_parsers.exc.InputParserUseFailureExc import InputParserUseFailureExc
from spideriment_ng_search.mvc.models.ModelIface import ModelIface
from spideriment_ng_search.mvc.models.exc.ModelUseFailureExc import ModelUseFailureExc
from spideriment_ng_search.mvc.views.SuccessViewIface import SuccessViewIface
from spideriment_ng_search.mvc.views.ErrorViewIface import ErrorViewIface


Controller_ParsedInput_T = TypeVar("Controller_ParsedInput_T")
Controller_ModelOutput_T = TypeVar("Controller_ModelOutput_T")


class Controller(Generic[Controller_ParsedInput_T, Controller_ModelOutput_T]):
    def __init__(self,
                 input_parser: InputParserIface[Controller_ParsedInput_T],
                 model: ModelIface[Controller_ParsedInput_T, Controller_ModelOutput_T],
                 success_view: SuccessViewIface[Controller_ParsedInput_T, Controller_ModelOutput_T],
                 error_view: ErrorViewIface[Controller_ParsedInput_T]
                 ):
        self._input_parser: Final[InputParserIface[Controller_ParsedInput_T]] = input_parser
        self._model: Final[ModelIface[Controller_ParsedInput_T, Controller_ModelOutput_T]] = model
        self._success_view: Final[SuccessViewIface[Controller_ParsedInput_T, Controller_ModelOutput_T]] = success_view
        self._error_view: Final[ErrorViewIface[Controller_ParsedInput_T]] = error_view

    def use_controller(self, request: flask.Request) -> flask.Response:
        try:
            parsed_input = self._use_input_parser(request)
        except InputParserUseFailureExc as e:
            return self._use_error_view(None, e.get_user_readable_error_message(), e.may_show_intro_page())

        try:
            model_output = self._use_model(parsed_input)
        except ModelUseFailureExc as f:
            return self._use_error_view(parsed_input, f.get_user_readable_error_message(), f.may_show_intro_page())

        return self._use_success_view(parsed_input, model_output)

    def _use_input_parser(self, request: flask.Request) -> Controller_ParsedInput_T:
        # For future extension.
        return self._input_parser.use_input_parser(request)

    def _use_model(self, parsed_input: Controller_ParsedInput_T) -> Controller_ModelOutput_T:
        # For future extension.
        return self._model.use_model(parsed_input)

    def _use_success_view(self, parsed_input: Controller_ParsedInput_T, model_output: Controller_ModelOutput_T) -> flask.Response:
        # For future extension.
        return self._success_view.use_success_view(parsed_input, model_output)

    def _use_error_view(self, optional_parsed_input: Optional[Controller_ParsedInput_T], user_readable_error_message: str, may_show_intro_page: bool) -> flask.Response:
        # For future extension.
        return self._error_view.use_error_view(optional_parsed_input, user_readable_error_message, may_show_intro_page)
