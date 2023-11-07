#!/usr/bin/python3
"""function that writes a string to a text file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
