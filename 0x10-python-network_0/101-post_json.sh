#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sX POST -H "Conenet-Type: application/json" -d @"$2" "$1"
