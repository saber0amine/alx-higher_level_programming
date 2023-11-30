#!/bin/bash
# send GET request with customized header
curl -s -X GET --header "X-HolbertonSchool-User-Id: 98" "$1"
