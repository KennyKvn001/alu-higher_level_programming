#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

<<<<<<< HEAD
=======
    
>>>>>>> 7942fb7647ee3e9c1019786669645d7488a49fb2
    avg = 0
    size = 0
    for x in my_list:
        avg += (x[0] * x[1])
        size += x[1]
    return avg / size
