#!/bin/bash
# This script sends a request to an URL
curl -s "$1":5000 |wc -c
