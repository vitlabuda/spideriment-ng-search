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


from typing import Generic
import abc
from spideriment_ng_search.databases.drivers.exc.DatabaseBaseExc import DatabaseBaseExc
from spideriment_ng_search.mvc.models.ModelIface import ModelIface, Model_ParsedInput_T, Model_ModelOutput_T
from spideriment_ng_search.mvc.models.exc.ModelUseFailureExc import ModelUseFailureExc


class _DefaultModelBase(ModelIface[Model_ParsedInput_T, Model_ModelOutput_T], Generic[Model_ParsedInput_T, Model_ModelOutput_T], metaclass=abc.ABCMeta):
    def _generate_surrogate_for_database_exception(self, database_exception: DatabaseBaseExc) -> ModelUseFailureExc:
        return ModelUseFailureExc(
            model_class_name=self.__class__.__name__,
            user_readable_error_message=database_exception.get_user_readable_error_message(),
            may_show_intro_page=False
        )
