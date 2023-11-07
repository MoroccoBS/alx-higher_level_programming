#!/usr/bin/python3
"""function that adds all arguments to a Python list"""
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def add_item_json_file():
    """adds all arguments to a Python list"""
    args = sys.argv[1:]
    my_list = load_from_json_file("add_item.json")
    for arg in args:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    add_item_json_file()
