#!/usr/bin/python3
""" function that adds all arguments to a Python list """


def pascal_triangle(n):
    """
    creates a pascal triangle
    """
    tri = []
    if n <= 0:
        return tri
    for i in range(n):
        tri.append([])
        tri[i].append(1)
        for j in range(1, i):
            tri[i].append(tri[i - 1][j - 1] + tri[i - 1][j])
        if i != 0:
            tri[i].append(1)
    return tri
