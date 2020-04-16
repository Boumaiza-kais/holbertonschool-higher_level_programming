#!/usr/bin/python3
"""
Python script
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    print(requests.get(url, auth=(username, password)).json().get('id'))
