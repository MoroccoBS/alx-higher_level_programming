#!/usr/bin/python3
""" MyInt module"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
