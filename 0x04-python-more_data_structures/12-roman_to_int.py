#!/usr/bin/python3
def roman_to_int(roman_string):
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    n = len(roman_string)
    i = n - 1
    output = 0
    while i >= 0:
        if i < n - 1 and map[roman_string[i]] < map[roman_string[i + 1]]:
            output -= map[roman_string[i]]
        else:
            output += map[roman_string[i]]
        i -= 1
    return output
