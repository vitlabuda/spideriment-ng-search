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


from typing import Final, Generic, Any, Callable
import abc
import flask
from spideriment_ng_search.exc.ThisShouldNeverHappenError import ThisShouldNeverHappenError
from spideriment_ng_search.mvc.input_parsers.InputParserIface import InputParserIface, InputParser_ParsedInput_T
from spideriment_ng_search.mvc.input_parsers.InputDictSource import InputDictSource
from spideriment_ng_search.mvc.input_parsers.exc.InputParserUseFailureExc import InputParserUseFailureExc


class _DefaultInputParserBase(InputParserIface[InputParser_ParsedInput_T], Generic[InputParser_ParsedInput_T], metaclass=abc.ABCMeta):
    def __init__(self, input_dict_source: InputDictSource):
        self._input_dict_source_method: Final[Callable[[flask.Request], Any]] = self._get_appropriate_input_dict_source_method_as_per_enum(input_dict_source)

    def _get_appropriate_input_dict_source_method_as_per_enum(self, input_dict_source: InputDictSource) -> Callable[[flask.Request], Any]:
        try:
            return ({
                InputDictSource.GET_PARAMS: self._get_input_dict_from_get_params,
                InputDictSource.POST_PARAMS: self._get_input_dict_from_post_params,
                InputDictSource.JSON_BODY: self._get_input_dict_from_json_body
            }[input_dict_source])
        except KeyError:
            raise ThisShouldNeverHappenError(f"Invalid input dict source enum value: {repr(input_dict_source)}")

    def use_input_parser(self, request: flask.Request) -> InputParser_ParsedInput_T:
        input_dict = self._input_dict_source_method(request)

        return self._use_input_parser_on_dict(input_dict)

    @abc.abstractmethod
    def _use_input_parser_on_dict(self, input_dict: Any) -> InputParser_ParsedInput_T:
        """
        The type of 'input_dict' is specified as 'Any', because the type of the variable is not validated. This method
         is supposed to validate it, and if it is not 'dict', this method should raise an appropriate exception.
        """

        raise NotImplementedError(self.__class__._use_input_parser_on_dict.__qualname__)

    def _get_input_dict_from_get_params(self, request: flask.Request) -> Any:
        # For future extension.
        return request.args

    def _get_input_dict_from_post_params(self, request: flask.Request) -> Any:
        # For future extension.
        return request.form

    def _get_input_dict_from_json_body(self, request: flask.Request) -> Any:
        # For future extension.
        return request.json

    def _generate_no_input_exception(self) -> InputParserUseFailureExc:  # DP: Factory:
        return InputParserUseFailureExc(
            input_parser_class_name=self.__class__.__name__,
            user_readable_error_message="The request does not contain any input parameters!",
            may_show_intro_page=True
        )

    def _generate_input_parsing_failure_exception(self, input_parameter_name: str, error_description: str) -> InputParserUseFailureExc:  # DP: Factory
        return InputParserUseFailureExc(
            input_parser_class_name=self.__class__.__name__,
            user_readable_error_message=f"An error occurred while parsing the {repr(input_parameter_name)} input parameter: {error_description}",
            may_show_intro_page=False
        )
