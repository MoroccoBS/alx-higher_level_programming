#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Function that prints the list in ascending order"""
        print(sorted(self))
