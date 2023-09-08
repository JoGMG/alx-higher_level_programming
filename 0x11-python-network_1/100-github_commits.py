#!/usr/bin/python3
""" A Python script that lists the 10 most recent commits of a given
    GitHub repository.
    - Using the `requests` package.
    - The first argument will be the `repository name`
    - The second argument will be the `owner name`

"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
