#!/usr/bin/python3
""" A Python script that takes in a URL and an email address,
    sends a `POST` request to the passed URL with the email as
    a parameter, and finally displays the body of the response.
    - Using the `requests` package.
    - The email must be sent in the variable `email`
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
