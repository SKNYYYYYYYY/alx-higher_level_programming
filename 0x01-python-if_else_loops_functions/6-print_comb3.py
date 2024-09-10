#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        # Print numbers followed by a comma and space, except for the last one
        if i == 8 and j == 9:
            print("{:02}".format(i * 10 + j))
        else:
            print("{:02}, ".format(i * 10 + j), end="")
