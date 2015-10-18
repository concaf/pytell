#!/usr/bin/python3

import os
import sys

def ls():
    try:
        return os.listdir(sys.argv[1])
    except IndexError:
        return os.listdir()

if __name__ == "__main__":
    ls_output = ls()

    for content in ls_output:
        print(content)