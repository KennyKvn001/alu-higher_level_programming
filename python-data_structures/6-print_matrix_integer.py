#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            print("{:d}".format(matrix[c][r]))
            if r != len(metrix[c]):
                print(" ", end="")
        print("")
