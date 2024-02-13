#!/usr/bin/python3
"""
script that takes in URL, sends request to URL
and displays value of X-Request-Id variable found in header
of response.
"""
import urllib.request
import sys


def print_header(url):
    """Prints value of X-Request-Id header in response."""
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    print_header(url)
