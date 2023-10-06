#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        i = 0
        for number in index:
            i += 1
            print("{}".format(number), end=" " if i < len(index) else "")
        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
