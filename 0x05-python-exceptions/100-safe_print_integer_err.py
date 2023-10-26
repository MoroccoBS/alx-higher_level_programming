#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as e:
        print("Exception: {}".format(e), file=stderr)
        return False
    except ValueError as e:
        print("Exception: {}".format(e), file=stderr)
        return False