#!/bin/bash
# Sends a request and displays the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
