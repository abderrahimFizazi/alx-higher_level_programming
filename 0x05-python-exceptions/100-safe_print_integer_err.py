#!/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as er:
        import sys
        print("Exception: {}".format(er), file=sys.stderr)
        return False
