#!/usr/bin/python3
import sys
num = len(sys.argv)
counter = 1
if num  == 1:
    print("{} argument.".format(num - 1))
elif num > 1:
    print("{} arguments:" .format(num - 1))
    while counter < num:
        print("{}: {}" .format(counter, sys.argv[counter]))
        counter += 1
