#!/bin/bash
# send json file
curl -X PUT -d "user_id=98" --header "Origin: HolbertonSchool" -sL 0:5000/catch_me
