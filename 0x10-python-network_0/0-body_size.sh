#!/bin/bash
#script to print the side of the body of a http header response
url="$1"
body_size=$(curl -I -s -w "%{size_download}" -o /dev/null "$url")
echo "$body_size"

