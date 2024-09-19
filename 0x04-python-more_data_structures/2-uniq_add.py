#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = []
    [new_list.append(x) for x in my_list if x not in new_list]
    for i in range(len(new_list)):
        sum += new_list[i]
    return sum
