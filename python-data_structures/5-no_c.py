#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        new = [x if x != "c" or x != "C" else (my_string)]
        return (new)
