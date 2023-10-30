#!/usr/bin/python3
"""Module for add_integer function"""


def add_integer(a, b=98):
    """Add two integers

        Args:
                a: first integer
                b: second integer

    Raises:
                TypeError: if a or b is not an integer
        Returns:
                The return value. a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")
