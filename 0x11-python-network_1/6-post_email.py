#!/usr/bin/python3
"""
Python script
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    print(requests.post(url, data={"email": email}).text)
