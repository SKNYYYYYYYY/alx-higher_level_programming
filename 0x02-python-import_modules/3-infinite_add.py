#!/usr/bin/python3
import sys


def main():
    sum = 0
    counter = 0
    num = len(sys.argv)

    while counter < num - 1:
        sum += int(sys.argv[counter + 1])
        counter += 1
    print(sum)


if __name__ == "__main__":
    main()
