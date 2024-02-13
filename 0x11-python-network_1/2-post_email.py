#!/usr/bin/python3
"""
Send POST request to given URL with email as parameter and displays
body of response.
"""

import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')

    print(content)
