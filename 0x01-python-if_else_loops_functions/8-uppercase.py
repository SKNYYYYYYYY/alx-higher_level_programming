#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase
            r = chr(ord(char) - 32)
        else:
            r = char
        print("{}".format(r), end="")
    print()  # Print a newline character after the complete string
