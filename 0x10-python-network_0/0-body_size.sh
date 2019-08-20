#!/bin/bash
# This script sends a request to an URL
curl -s "$1" |wc -c
