#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number in range(-9, 10):
    last_d = number
else:
    last_d = abs(number) % 10  # Get the absolute value of the last digit
    if number < 0:
        last_d = -last_d  # Keep the negative sign if the number is negative

if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
elif last_d < 6 and last_d != 0:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
