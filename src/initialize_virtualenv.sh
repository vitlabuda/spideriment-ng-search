#!/bin/bash

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


SNGS_VIRTUALENV_PATH="./__venv__"
SNGS_REQUIREMENTS_FILE_PATH="./requirements.txt"


function sngs_exit_with_error() {
  local __ERROR_MESSAGE__="$1"

  echo "# ERROR: ${__ERROR_MESSAGE__}"
  exit 1
}

function sngs_print_info_message() {
  local __INFO_MESSAGE__="$1"

  echo "# INFO: ${__INFO_MESSAGE__}"
}


# Traverse into the directory where this script is located
cd -- "$(dirname -- "$0")" || sngs_exit_with_error "Failed to traverse into the directory where this script is located!"


# Perform necessary checks
if [ ! -f "${SNGS_REQUIREMENTS_FILE_PATH}" ]; then
  sngs_exit_with_error "The requirements file is missing on path '${SNGS_REQUIREMENTS_FILE_PATH}'!"
fi

if [ -d "${SNGS_VIRTUALENV_PATH}" ]; then
  sngs_exit_with_error "The virtualenv directory already exists on path '${SNGS_VIRTUALENV_PATH}'!"
fi


# Initialize the virtual environment
sngs_print_info_message "Initializing the program's Python virtual environment, please wait..."

virtualenv -p python3 "${SNGS_VIRTUALENV_PATH}" > /dev/null || sngs_exit_with_error "Failed to create the program's Python virtual environment!"
. "${SNGS_VIRTUALENV_PATH}/bin/activate" > /dev/null || sngs_exit_with_error "Failed to activate the program's Python virtual environment!"
"${SNGS_VIRTUALENV_PATH}/bin/pip3" install -r "${SNGS_REQUIREMENTS_FILE_PATH}" > /dev/null || sngs_exit_with_error "Failed to install the required libraries into the program's Python virtual environment!"

sngs_print_info_message "The program's Python virtual environment has been initialized successfully!"
