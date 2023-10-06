#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    return tuple_a[1], tuple_b


tuple_a = (1, 89)
tuple_b = (88, 11)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)

print(add_tuple(tuple_a, tuple_a))
# print(add_tuple(tuple_a, ()))
