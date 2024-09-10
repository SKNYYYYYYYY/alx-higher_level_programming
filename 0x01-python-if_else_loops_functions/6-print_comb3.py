#!/usr/bin/python3

for i in range(0, 100):
    last_digit = i % 10
    first_digit = (i - last_digit) / 10
    interchanged = (last_digit * 10) + first_digit
    if i < interchanged:
        print(i)