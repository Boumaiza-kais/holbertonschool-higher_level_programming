#!/usr/bin/python3
"""
Python script
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    reps = requests.get(url)
    if reps.status_code >= 400:
        print("Error code: {}".format(reps.status_code))
    else:
        print(reps.text)
