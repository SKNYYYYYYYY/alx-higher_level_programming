#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            if isinstance(i, int):
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except (TypeError, ValueError):
            continue
    print()
    return counter
