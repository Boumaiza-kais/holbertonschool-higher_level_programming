#!/bin/bash
# Bash script
curl -so "$1" /dev/null -w '%{http_code}'
