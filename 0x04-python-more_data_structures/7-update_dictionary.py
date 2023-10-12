#!/usr/bin/python3
print_sorted_dictionary = __import__(
    "6-print_sorted_dictionary"
).print_sorted_dictionary


def update_dictionary(a_dictionary: dict, key: str, value: any):
    new_dict = a_dictionary.copy()
    new_dict[key] = value
    return new_dict
