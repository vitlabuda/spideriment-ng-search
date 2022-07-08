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


from typing import Generic, TypeVar, Optional
import abc
import flask
from spideriment_ng_search.mvc.views.SuccessViewIface import SuccessViewIface
from spideriment_ng_search.mvc.views.ErrorViewIface import ErrorViewIface


WebView_ParsedInput_T = TypeVar("WebView_ParsedInput_T")
WebView_ModelOutput_T = TypeVar("WebView_ModelOutput_T")


class _DefaultWebViewBase(SuccessViewIface[WebView_ParsedInput_T, WebView_ModelOutput_T], ErrorViewIface[WebView_ParsedInput_T], Generic[WebView_ParsedInput_T, WebView_ModelOutput_T], metaclass=abc.ABCMeta):
    def use_success_view(self, parsed_input: WebView_ParsedInput_T, model_output: WebView_ModelOutput_T) -> flask.Response:
        return self._render_flask_template(
            optional_parsed_input=parsed_input,
            optional_model_output=model_output,
            optional_error_message=None
        )

    def use_error_view(self, optional_parsed_input: Optional[WebView_ParsedInput_T], user_readable_error_message: str, may_show_intro_page: bool) -> flask.Response:
        return self._render_flask_template(
            optional_parsed_input=optional_parsed_input,
            optional_model_output=None,
            optional_error_message=(None if may_show_intro_page else user_readable_error_message)
        )

    def _render_flask_template(self, optional_parsed_input: Optional[WebView_ParsedInput_T], optional_model_output: Optional[WebView_ModelOutput_T], optional_error_message: Optional[str]) -> flask.Response:
        return flask.make_response(flask.render_template(
            self._get_flask_template_filename(),
            optional_parsed_input=optional_parsed_input,
            optional_model_output=optional_model_output,
            optional_error_message=optional_error_message
        ))

    @abc.abstractmethod
    def _get_flask_template_filename(self) -> str:
        raise NotImplementedError(self.__class__._get_flask_template_filename.__qualname__)
