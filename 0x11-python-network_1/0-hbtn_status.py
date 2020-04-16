#!/usr/bin/python3
"""
Python script
"""

import urllib.request
import urllib

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        rp_read = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(rp_read)))
        print("\t- content: {}".format(rp_read))
        print("\t- utf8 content: {}".format(rp_read.decode('utf-8')))
