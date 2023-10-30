#!/usr/bin/python3
"""Module for function that prints <first name> <last name>."""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>.
    Args:
                first_name: first name
                last_name: last name
    Raises:
                TypeError: if first_name or last_name is not a string
    Returns:
                None

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/3-say_my_name.txt")
