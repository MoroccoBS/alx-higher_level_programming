#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def multiply_helper(item):
        return item * number

    new_list = map(multiply_helper, my_list)
    return list(new_list)
