#!/usr/bin/python3
""" Write a Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your `id`
    - Using the `requests` package.
    - You must use Basic Authentication with a personal access token as password to
      access to your information (only `read:user` permission is needed)
    - The first argument will be your `username`
    - The second argument will be your `password` (in your case,
      a personal access token as password)
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
