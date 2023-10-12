#!/usr/bin/python3
def complex_delete(a_dictionary: dict, value):
    keys_to_delete = []
    for key, values in a_dictionary.items():
        if value == values:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
