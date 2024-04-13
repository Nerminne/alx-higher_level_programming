#!/bin/bash
#script that takes in a URL, and displays the body of the response
#script that takes in a URL, and displays the body of the response
d=$(curl -sI "$1")
if echo "$d" | grep -q "200 OK"; then
  curl -s "$1"
fi
