#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    # result = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    # for i in new_list:
    #     result += i
    return sum(new_list)
