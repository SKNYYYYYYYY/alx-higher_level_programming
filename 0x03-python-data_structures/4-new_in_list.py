#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return cp_list
    else:
        cp_list.insert(idx, element)
        del cp_list[idx + 1]
        return cp_list
