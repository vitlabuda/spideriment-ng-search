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


from datalidator.blueprints.extras.ObjectModel import ObjectModel
from datalidator.blueprints.impl.IntegerBlueprint import IntegerBlueprint
from datalidator.blueprints.impl.StringBlueprint import StringBlueprint
from datalidator.filters.impl.StringUnifyWhitespaceFilter import StringUnifyWhitespaceFilter
from datalidator.filters.impl.StringDeduplicateWhitespaceFilter import StringDeduplicateWhitespaceFilter
from datalidator.filters.impl.StringStripFilter import StringStripFilter
from datalidator.validators.impl.IntegerIsPositiveValidator import IntegerIsPositiveValidator
from datalidator.validators.impl.NumberMaximumValueValidator import NumberMaximumValueValidator
from datalidator.validators.impl.SequenceIsNotEmptyValidator import SequenceIsNotEmptyValidator
from datalidator.validators.impl.StringContainsNoControlOrSeparatorCharactersValidator import StringContainsNoControlOrSeparatorCharactersValidator
from spideriment_ng_search.SpiderimentSearchConstants import SpiderimentSearchConstants


_MAX_LENGTH_BLUEPRINT = IntegerBlueprint(
    validators=(IntegerIsPositiveValidator(),)
)


class _WebViewConfigModel(ObjectModel):
    document_search_title_max_length = _MAX_LENGTH_BLUEPRINT
    document_search_snippet_max_length = _MAX_LENGTH_BLUEPRINT
    image_search_description_max_length = _MAX_LENGTH_BLUEPRINT

    default_max_search_results = IntegerBlueprint(
        validators=(
            IntegerIsPositiveValidator(),
            NumberMaximumValueValidator(SpiderimentSearchConstants.MAX_RESULTS_LIMIT)
        )
    )

    datetime_format_specification = StringBlueprint(
        filters=(
            StringUnifyWhitespaceFilter(replacement_whitespace=" "),
            StringDeduplicateWhitespaceFilter(),
            StringStripFilter()
        ),
        validators=(
            SequenceIsNotEmptyValidator(),
            StringContainsNoControlOrSeparatorCharactersValidator(allowed_characters=" ")
        )
    )
