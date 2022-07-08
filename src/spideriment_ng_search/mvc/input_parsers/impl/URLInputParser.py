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
from datalidator.exc.DatalidatorExc import DatalidatorExc
from datalidator.blueprints.impl.ObjectBlueprint import ObjectBlueprint
from spideriment_ng_search.mvc.input_parsers._DefaultInputParserBase import _DefaultInputParserBase
from spideriment_ng_search.mvc.input_parsers.impl._models._URLModel import _URLModel  # noqa


class URLInputParser(_DefaultInputParserBase[str]):
    _URL_BLUEPRINT: Final[ObjectBlueprint] = ObjectBlueprint(_URLModel, tag="__input_dict__")

    def _use_input_parser_on_dict(self, input_dict: Any) -> str:
        if not input_dict:
            raise self._generate_no_input_exception()

        try:
            url_model = self.__class__._URL_BLUEPRINT.use(input_dict)
        except DatalidatorExc as e:
            raise self._generate_input_parsing_failure_exception(e.get_originator_tag(), str(e))

        return url_model.url
