#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            i = ord(char) - 32
            r = chr(i)
        else:
            r = char
        print(f"{r}", end="")
    print("\n")