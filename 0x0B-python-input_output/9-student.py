#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """
    class Student that defines a student
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
