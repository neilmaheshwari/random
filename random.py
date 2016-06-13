#! /usr/bin/env python3

import sys

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Hello")
    elif (sys.argv[1] == "test"):
        print("Running tests")
    else:
        print("Unexpected input")
