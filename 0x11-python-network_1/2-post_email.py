#!/usr/bin/python3
""" A Python script that takes in a URL and an email, sends a `POST` request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in `utf-8`).
    - The email must be sent in the `email` variable.
    - Using the urllib package.
"""
from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
