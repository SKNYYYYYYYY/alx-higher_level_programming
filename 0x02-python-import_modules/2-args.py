#!/usr/bin/python3
import sys


def main():
    num = len(sys.argv)
    counter = 1
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
        print("{}: {}" .format(counter, sys.argv[counter]))

    elif num > 2:
        print("{} arguments:" .format(num - 1))
        while counter < num:
            print("{}: {}" .format(counter, sys.argv[counter]))
            counter += 1


if __name__ == "__main__":
    main()
