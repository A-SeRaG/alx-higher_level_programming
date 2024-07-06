#!/usr/bin/python3
"""Python script that takes in a URL,
    sends a request to the URL and displays the body of
    the response (decoded in utf-8)."""

from sys import argv
from urllib import request, error


if __name__ = "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as er:
        print('Error code: ', er.code)
