#!/bin/bash
# Bash script
curl -so /dev/null -w '%{response_code}' "$1"
