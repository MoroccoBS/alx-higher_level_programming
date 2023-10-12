#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict):
    keys = a_dictionary.keys()
    sorted_list = sorted(keys)
    for i in sorted_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
