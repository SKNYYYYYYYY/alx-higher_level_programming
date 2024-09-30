#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in my_list:
            if counter < x:
                print(i, end="")
                counter += 1
            else:
                break
        print()
    except IndexError:
        print("Error while printing list")
    return counter
