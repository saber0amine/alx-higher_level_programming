#!/bin/bash
# displays the size of the response's body
curl -s "$1" | wc -c
