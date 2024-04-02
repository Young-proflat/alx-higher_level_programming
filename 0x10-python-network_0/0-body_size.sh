#!/bin/bash
# Takes in a URL, sends a request to that URL and displays the size in byte
curl -sI $1 | grep "Content-length" | cut -d " " -f2
