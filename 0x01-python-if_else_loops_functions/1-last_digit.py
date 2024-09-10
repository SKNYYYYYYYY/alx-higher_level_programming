#!/usr/bin/python3
import random
number = random.randint(-10, 10)
last_d = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
