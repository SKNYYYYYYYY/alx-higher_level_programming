#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:    
        checker = 0
        if len(my_list) == 0:
            return None
        for i in my_list:
            if i > checker:
                checker = i
        return checker
    else:
        return None
