#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    checker = my_list[0]  # Initialize checker to the first element of the list
    for i in my_list:
        if i > checker:
            checker = i  # Update checker if a larger integer is found

    return checker
