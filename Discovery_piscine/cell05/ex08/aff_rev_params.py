#!/usr/bin/python3

#Cell 5-8 - Python

import sys

params = sys.argv[1:]

if len(params) < 2:
    print("None")
else:
    for param in reversed(params):
        print(param)

        