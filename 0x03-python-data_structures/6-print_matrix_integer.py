#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        i = 0
        for number in index:
            i += 1
            print("{}".format(number), end=" " if i < len(index) else "")
        print()
