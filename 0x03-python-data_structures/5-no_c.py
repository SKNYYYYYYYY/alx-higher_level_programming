#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    new = []
    for i in my_string:
        if i not in ('c', 'C'):
            new_string.append(i)
    return "".join(new_string)
