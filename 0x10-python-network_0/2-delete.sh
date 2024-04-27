#!/bin/bash
#Script rto send a delete request to a url and display response body
curl -s -X DELETE "$1" -o response.txt && cat response.txt; echo ""
