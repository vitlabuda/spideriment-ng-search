#!/bin/bash

SPIDERIMENT_SEARCH_HOST="http://127.0.0.1:5000"



##### Example 1 - Image search with search results #####
curl --request POST --header 'Content-Type: application/json' --data '{"search_query": "opengl", "max_results": 5}' "${SPIDERIMENT_SEARCH_HOST}/api/image-search"

# {
#  "data": {
#    "search_results": [
#      {
#        "description": "Linux kernel and OpenGL video games.svg",
#        "score": 2444.3205070495605,
#        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Linux_kernel_and_OpenGL_video_games.svg/220px-Linux_kernel_and_OpenGL_video_games.svg.png"
#      }
#    ]
#  },
#  "success": true
# }



##### Example 2 - Image search with no search results #####
curl --request POST --header 'Content-Type: application/json' --data '{"search_query": "asfdkjfjansdhjfajksndf", "max_results": 5}' "${SPIDERIMENT_SEARCH_HOST}/api/image-search"

# {
#  "data": {
#    "search_results": []
#  },
#  "success": true
# }



##### Example 3 - Image search failure #####
curl --request POST --header 'Content-Type: application/json' --data '{"search_query": "", "max_results": 5}' "${SPIDERIMENT_SEARCH_HOST}/api/image-search"

# {
#  "error_message": "An error occurred while parsing the 'search_query' input parameter: The input sequence is empty!",
#  "success": false
# }
