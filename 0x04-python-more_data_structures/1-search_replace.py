#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    cp_my_list = my_list[:]
    for i in range(len(cp_my_list)):
        if cp_my_list[i] == search:
            cp_my_list[i] = replace
        new_list.append(cp_my_list[i])
    return new_list
