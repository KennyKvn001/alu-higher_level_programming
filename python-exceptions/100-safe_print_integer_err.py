#!/usr/bin/python3
def safe_print_integer_err(value):
    print("{:d}".format(value))
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
