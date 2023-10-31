#!/usr/bin/python3
"""A class that prevents the user from instantiating new attributes"""


class LockedClass:
    """A class that prevents the user from instantiating new attributes"""

    __slots__ = ["first_name"]
