#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    else:
        for m in range(len(my_list)):
            m = max(my_list)
            print(":d".format(my_list[m]))

