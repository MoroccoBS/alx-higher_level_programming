#!/usr/bin/python3
"""Module for matrix divided function"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix by div.

    Args:
                matrix: matrix to be divided
                div: divisor

    Raises:
                TypeError: if matrix is not a matrix
                ZeroDivisionError: if div is zero

    Returns:
                The return value. matrix divided by div
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers")
    if not all(isinstance(elem, int) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers")
    if not isinstance(div, int) or div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
