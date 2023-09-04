#!/bin/bash
# Displays the byte size of the body of a response.
curl -s "$1" | wc -c
