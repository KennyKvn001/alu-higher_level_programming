#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    else:
        for max in my_list:
            print("{:d}".format(max))

