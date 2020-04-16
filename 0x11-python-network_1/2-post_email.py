#!/usr/bin/python3
"""
Python script
"""

import urllib.request
import urllib
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    req = urllib.request.Request(url, data.encode('utf-8'))
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
