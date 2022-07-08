#!/bin/bash

SPIDERIMENT_SEARCH_HOST="http://127.0.0.1:5000"



##### Example 1 - Document search with search results #####
curl --request POST --header 'Content-Type: application/json' --data '{"search_query": "linux kernel", "max_results": 5}' "${SPIDERIMENT_SEARCH_HOST}/api/document-search"

# {
#  "data": {
#     "search_results": [
#       {
#         "score": 30360.891456604004,
#         "snippet": "They're not...well they are, and they're not. There is no single kernel. Every single distribution has their own changes. That's been going on since pretty much day one. I don't know if you may remember Yggdrasil was known for having quite extreme changes to the kernel and even today all of the major vendors have their own tweaks because they have some portion of the market they're interested in and quite frankly that's how it should be. Because if everybody expects one person, me, to be able to track everything that's not the point of GPL. That's not the point of having an open system. So actually the fact that a distribution decides that something is so important to them that they will add patches for even when it's not in the standard kernel, that's a really good sign for me. So that's for example how something like ReiserFS got added. And the reason why ReiserFS is the first journaling filesystem that was integrated in the standard kernel was not because I love Hans Reiser. It was because SUSE actually started shipping with ReiserFS as their standard kernel, which told me \"ok.\" This is actually in production use. Normal People are doing this. They must know something I don't know. So in a very real sense what a lot of distribution houses do, they are part of this \"let's make our own branch\" and \"let's make our changes to this.\" And because of the GPL, I can take the best portions of them.[277]",
#         "title": "Linux kernel - Wikipedia",
#         "url": "https://en.wikipedia.org/wiki/Linux_kernel"
#       },
#       {
#         "score": 23217.849941253662,
#         "snippet": "A hybrid kernel is an operating system kernel architecture that attempts to combine aspects and benefits of microkernel and monolithic kernel architectures used in computer operating systems.[1][2]",
#         "title": "Hybrid kernel - Wikipedia",
#         "url": "https://en.wikipedia.org/wiki/Hybrid_kernel"
#       },
#       {
#         "score": 23211.7578125,
#         "snippet": "The Linux kernel mailing list (LKML) is the main electronic mailing list for Linux kernel development,[1][2] where the majority of the announcements, discussions, debates, and flame wars over the kernel take place.[3] Many other mailing lists exist to discuss the different subsystems and ports of the Linux kernel, but LKML is the principal communication channel among Linux kernel developers.[4] It is a very high-volume list, usually receiving about 1,000 messages each day, most of which are kernel code patches.",
#         "title": "Linux kernel mailing list - Wikipedia",
#         "url": "https://en.wikipedia.org/wiki/Linux_kernel_mailing_list"
#       },
#       {
#         "score": 17924.511070251465,
#         "snippet": "Following Linus' reply, Tanenbaum argued that the limitations of MINIX relate to him being a professor, stating the requirement for the system to be able to run on the rather limited hardware of the average student, which he noted was an Intel 8088-based computer, sometimes even without a hard drive.[4] Linux was, at that time, specifically built for the Intel 386, a significantly more powerful (and expensive) processor. Tanenbaum also specifically states \"... as of about 1 year ago, there were two versions [of MINIX], one for the PC (360K diskettes) and one for the 286/386 (1.2M). The PC version was outselling the 286/386 version by 2 to 1.\" He noted that even though Linux was free, it wouldn't be a viable choice for his students, as they would not be able to afford the expensive hardware required to run it, and that MINIX could be used on \"a regular 4.77 MHz PC with no hard disk.\" To this, Kevin Brown, another user of the Usenet group, replied that Tanenbaum should not complain about Linux's ties to the 386 architecture, as it was the result of a conscious choice rather than lack of knowledge about operating system design, stating \"... an explicit design goal of Linux was to take advantage of the special features of the 386 architecture. So what exactly is your point? Different design goals get you different designs.\"[5] He also stated that designing a system specifically for cheap hardware would cause it to have portability problems in the future. Despite the fact that MINIX did not fully support the newer h",
#         "title": "Tanenbaum–Torvalds debate - Wikipedia",
#         "url": "https://en.wikipedia.org/wiki/Tanenbaum-Torvalds_debate"
#       },
#       {
#         "score": 17600.254974365234,
#         "snippet": "Mac OS X 10.6 is the first version of macOS that supports a 64-bit kernel. However, not all 64-bit computers can run the 64-bit kernel, and not all 64-bit computers that can run the 64-bit kernel will do so by default.[86] The 64-bit kernel, like the 32-bit kernel, supports 32-bit applications; both kernels also support 64-bit applications. 32-bit applications have a virtual address space limit of 4 GiB under either kernel.[87][88] The 64-bit kernel does not support 32-bit kernel extensions, and the 32-bit kernel does not support 64-bit kernel extensions.",
#         "title": "x86-64 - Wikipedia",
#         "url": "https://en.wikipedia.org/wiki/X86-64"
#       }
#     ]
#   },
#   "success": true
# }



##### Example 2 - Document search with no search results #####
curl --request POST --header 'Content-Type: application/json' --data '{"search_query": "fkjdnsajfnasjdf", "max_results": 5}' "${SPIDERIMENT_SEARCH_HOST}/api/document-search"

# {
#  "data": {
#    "search_results": []
#  },
#  "success": true
# }



##### Example 3 - Document search failure #####
curl --request POST --header 'Content-Type: application/json' --data '{"search_query": "linux kernel", "max_results": -1}' "${SPIDERIMENT_SEARCH_HOST}/api/document-search"

# {
#  "error_message": "An error occurred while parsing the 'max_results' input parameter: The input integer is not positive: -1",
#  "success": false
# }
