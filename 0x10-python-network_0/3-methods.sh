#!/bin/bash
# get all allowed methods
curl -sI $1 | grep 'Allow: ' | sed 's/^.*: //'
