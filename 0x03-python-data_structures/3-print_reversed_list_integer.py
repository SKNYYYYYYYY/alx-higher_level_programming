#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = []
    my_list.reverse()
    rev = reversed_list.append(my_list)
    i = 0
    while i < len(rev):
        print("{:d}".format(reversed_list[i]))
        i += 1
