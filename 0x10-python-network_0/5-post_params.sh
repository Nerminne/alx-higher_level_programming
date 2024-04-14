#!/bin/bash
#script that takes URL, sends a POST and displays the body of the response
curl -s -X Post -d "email:test@gmail.com&subject=I will always be here for PLD" "$1"
