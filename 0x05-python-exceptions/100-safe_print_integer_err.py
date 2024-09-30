#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
            return False
    except ValueError:
        print("Error Encountered")
