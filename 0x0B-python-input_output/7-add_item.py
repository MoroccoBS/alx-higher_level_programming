#!/usr/bin/python3
"""function that adds all arguments to a Python list"""

import json
import sys


def add_item_json_file():
    """adds all arguments to a Python list"""
    args = sys.argv[1:]
    with open("add_item.json", "a") as f:
        if len(args) > 0:
            json.dump(args, f)
        else:
            json.dump([], f)


if __name__ == "__main__":
    add_item_json_file()
