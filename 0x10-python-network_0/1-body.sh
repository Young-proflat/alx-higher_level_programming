#!/bin/bash
#Takes in a URL,sends a request to that URL and displays the size of the body response
curl -sX GET $1 -L
