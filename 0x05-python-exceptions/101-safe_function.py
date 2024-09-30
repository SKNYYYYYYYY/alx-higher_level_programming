#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (TypeError, ZeroDivisionError, IndexError) as e:
        print("Exception: {}" .format(str(e)), file=sys.stderr)
        return None