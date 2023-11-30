#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Use curl to send a request and retrieve the size of the response body
response_size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')

# Check if Content-Length header is present in the response
if [ -z "$response_size" ]; then
    echo "Content-Length header not found in the response."
    exit 1
fi

# echo "Size of the response body: ${response_size} bytes"

echo "$response_size"
