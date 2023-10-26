#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A class that defines a square"""

    def size(self):
        return self.__size

    def __init__(self, size=0):
        self.__size = size

    def size(self, value):
        """Initialize a new square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
