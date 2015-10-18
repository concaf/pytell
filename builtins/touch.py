#!/usr/bin/python3

import os
import sys

def touch():
    for file_name in sys.argv[1:]:
        if os.path.islink(file_name):
            print("Link {} exists, updating timestamp now!".format(file_name))
            os.utime(file_name)
        elif os.path.isfile(file_name):
            print("File {} exists, updating timestamp now!".format(file_name))
            os.utime(file_name)
        elif os.path.isdir(file_name):
            print("Directory {} exists, updating timestamp now!".format(file_name))
            os.utime(file_name)
        elif os.path.ismount(file_name):
            print("Mount {} exists, updating timestamp now!".format(file_name))
            os.utime(file_name)
        elif not os.path.exists(file_name):
            print("Creating file and updating timestamp now!")
            new_file = open(file_name,mode='w')

if __name__ == "__main__":
    touch()