#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # for i in range(len(my_list)):
    #     print("{}".format(my_list[(i + 1) * -1]))
    for i in reversed(my_list):
        print("{}".format(i))
