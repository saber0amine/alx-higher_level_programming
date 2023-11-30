#!/bin/bash
# get content length from return header
curl -sI $1 | grep -i Content-length| awk '{print $2}'
