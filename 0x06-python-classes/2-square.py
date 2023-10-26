#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A class that defines a square"""

    __size = 0

    def __init__(self, size=0):
        """Initialize a new square size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
