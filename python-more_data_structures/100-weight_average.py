#!/usr/bin/python3
from functools import reduce
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list):
        return 0
    avg = 0
    size = 0
    for tup in my_list:
        avg += (tup[0] * tup[1])
        size += tup[1]
    return (avg / size)
