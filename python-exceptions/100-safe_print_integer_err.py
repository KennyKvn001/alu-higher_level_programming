#!/usr/bin/python3
def safe_print_integer_err(value):
    
    try:
        import sys

        print("{}".format(value))
        return True
    except (Exception, TypeError, ValueError):
        sys.stderr.write(f"Error: {ex}\n")
        return False
