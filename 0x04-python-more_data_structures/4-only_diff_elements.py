#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    intersection = set_1 & set_2
    for element in set_1.union(set_2):
        if element not in intersection:
            set_3.add(element)
    return set_3
