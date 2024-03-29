#!/usr/bin/python3
""" A Python script that takes in a URL, sends a request to
    the URL and displays the value of the variable `X-Request-Id`
    in the response header.
    - Using the `requests` package.
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
