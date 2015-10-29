#!/usr/bin/python3

import os
import sys

def cat():
    if len(sys.argv) == 1:
        pass
    else:
        for file_name in sys.argv[1:]:
            file_open = open(file_name, mode='r')
            print(file_open.read())

if __name__ == "__main__":
    cat()
