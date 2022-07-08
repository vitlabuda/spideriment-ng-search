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
from datalidator.blueprints.impl.FloatBlueprint import FloatBlueprint
from datalidator.validators.impl.NumberMinimumValueValidator import NumberMinimumValueValidator


_SCORE_BLUEPRINT = FloatBlueprint(
    allow_ieee754_special_values=False,
    validators=(NumberMinimumValueValidator(0.0),)
)


class _ScoringConfigModel(ObjectModel):
    min_total_score = _SCORE_BLUEPRINT

    title_score_multiplier = _SCORE_BLUEPRINT
    description_score_multiplier = _SCORE_BLUEPRINT
    heading_1_score_multiplier = _SCORE_BLUEPRINT
    heading_2_score_multiplier = _SCORE_BLUEPRINT
    heading_3_score_multiplier = _SCORE_BLUEPRINT
    heading_4_score_multiplier = _SCORE_BLUEPRINT
    heading_5_score_multiplier = _SCORE_BLUEPRINT
    emphasized_text_score_multiplier = _SCORE_BLUEPRINT
    regular_text_score_multiplier = _SCORE_BLUEPRINT
    list_item_text_score_multiplier = _SCORE_BLUEPRINT
    uncategorized_text_score_multiplier = _SCORE_BLUEPRINT
    fallback_text_score_multiplier = _SCORE_BLUEPRINT

    image_alt_text_score_multiplier = _SCORE_BLUEPRINT
    image_title_text_score_multiplier = _SCORE_BLUEPRINT
