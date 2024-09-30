#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    none_int = 0
    try:
        for i in my_list:
            if counter < x and isinstance(i, int):
                print("{:d}".format(i), end="")
                counter += 1
            else:
                none_int += 1
                continue
        print()
        if x - (counter + none_int) != 0 and counter != x:
            raise IndexError 
    except IndexError:
        print("Error")
    return counter
