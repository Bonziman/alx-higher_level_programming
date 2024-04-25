#!/bin/bash
url="$1"
body_size=$(curl -I -s -w "%{size_download}" -o /dev/null "$url")
echo "$body_size"

