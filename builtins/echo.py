#!/usr/bin/python3

import sys

def echo():
    if len(sys.argv) == 1:
        print("")
    else:
        for argument in sys.argv[1:]:
            print(argument,end=" ")

if __name__ == "__main__":
    echo()
    print()