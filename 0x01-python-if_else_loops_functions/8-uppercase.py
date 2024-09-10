#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            i = ord(char) - 32
            r = chr(i)
        else:
            r = char
        print("{}".format(r), end="")
    print("\n")
