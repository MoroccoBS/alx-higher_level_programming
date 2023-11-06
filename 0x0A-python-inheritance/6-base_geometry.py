#!/usr/bin/python3
""""BaseGeometry module"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")


bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
