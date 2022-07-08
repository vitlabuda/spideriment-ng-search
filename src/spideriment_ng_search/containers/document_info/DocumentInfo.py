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


from typing import Any
from dataclasses import dataclass
import datetime
from spideriment_ng_search.containers.ContainerIface import ContainerIface
from spideriment_ng_search.containers.document_info.ContentSnippet import ContentSnippet
from spideriment_ng_search.containers.document_info.Link import Link
from spideriment_ng_search.containers.document_info.Image import Image


@dataclass(frozen=True)
class DocumentInfo(ContainerIface):
    url: str
    title: str
    description: str
    filetype: str
    language: str
    author: str
    keywords: tuple[str, ...]
    content_snippets: tuple[ContentSnippet, ...]
    links: tuple[Link, ...]
    images: tuple[Image, ...]
    crawled_at: datetime.datetime

    def to_serializable_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "title": self.title,
            "description": self.description,
            "filetype": self.filetype,
            "language": self.language,
            "author": self.author,
            "keywords": list(self.keywords),
            "content_snippets": [content_snippet.to_serializable_dict() for content_snippet in self.content_snippets],
            "links": [link.to_serializable_dict() for link in self.links],
            "images": [image.to_serializable_dict() for image in self.images],
            "crawled_at": self.crawled_at.isoformat()
        }
