#!/bin/bash
# get status code
curl  -sI -o /dev/null -w '%{http_code}' "$1"
