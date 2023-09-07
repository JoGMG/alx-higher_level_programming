#!/bin/bash
# Sends a JSON `POST` request with contents of a file.
curl -s -H "Content-Type" -d "$2" "$1"
