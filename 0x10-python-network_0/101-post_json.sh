#!/bin/bash
# send json file
curl -s -X POST -d @"$2" --header "Content-Type: application/json" "$1"
