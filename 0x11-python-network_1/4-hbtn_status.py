#!/usr/bin/python3
"""
Python script
"""

import requests

if __name__ == "__main__":
    url_status = requests.get("https://intranet.hbtn.io/status")
    print('Body response:')
    print('\t- type:', type(url_status.text))
    print('\t- content:', url_status.text)
