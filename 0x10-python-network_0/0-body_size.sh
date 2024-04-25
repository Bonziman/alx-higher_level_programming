#!/bin/bash
#script to print the side of the body of a http header response
curl -s "$1" | wc -c
