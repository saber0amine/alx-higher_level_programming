#!/bin/bash
# Send GET request to URL and siplays the content of the response
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" $@
