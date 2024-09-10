#!/usr/bin/python3
def print_last_digit(number):
    if  number > 0:
        last_digitt = number % 10
        print(last_digitt, end="")
    else:
        number2 =  number * -1
        last_digitt = number2 % 10
        print(last_digitt, end="")
    return last_digitt