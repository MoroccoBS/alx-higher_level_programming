#!/usr/bin/python3
"""is_kind_of_class module"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    from the specified class otherwise False
    """
    return type(obj) != a_class and isinstance(obj, a_class)
