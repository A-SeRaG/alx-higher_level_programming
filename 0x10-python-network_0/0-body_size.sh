#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
response=$(curl -s -w "%{size_download}" -o /dev/null $1)
echo "Size of the response body: $response bytes"
