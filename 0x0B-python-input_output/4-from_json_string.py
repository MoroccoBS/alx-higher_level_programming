#!/usr/bin/python3
""" function that returns the JSON representation of an object (string) """


def from_json_string(my_str):
    import json

    return json.loads(my_str)
