#!/bin/bash
# send POST request
curl -s -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
