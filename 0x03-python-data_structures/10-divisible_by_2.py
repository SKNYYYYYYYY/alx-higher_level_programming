#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_my_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_my_list.append(True)
        else:
            new_my_list.append(False)

    print(new_my_list)
    return new_my_list