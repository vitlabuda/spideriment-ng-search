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


from spideriment_ng_search.exc.mixins.UserReadableErrorMessageExcMixin import UserReadableErrorMessageExcMixin
from spideriment_ng_search.exc.mixins.MayShowIntroPageExcMixin import MayShowIntroPageExcMixin
from spideriment_ng_search.mvc.input_parsers.exc.InputParserBaseExc import InputParserBaseExc


class InputParserUseFailureExc(InputParserBaseExc, UserReadableErrorMessageExcMixin, MayShowIntroPageExcMixin):
    def __init__(self, input_parser_class_name: str, user_readable_error_message: str, may_show_intro_page: bool):
        InputParserBaseExc.__init__(
            self=self,
            error_message=f"An error occurred while using the {repr(input_parser_class_name)} input parser: {user_readable_error_message}"
        )
        UserReadableErrorMessageExcMixin.__init__(
            self=self,
            user_readable_error_message=user_readable_error_message
        )
        MayShowIntroPageExcMixin.__init__(
            self=self,
            may_show_intro_page=may_show_intro_page
        )
