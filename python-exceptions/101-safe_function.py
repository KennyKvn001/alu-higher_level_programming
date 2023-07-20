#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        safe = fct(*args)
        return safe
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
