#!/usr/bin/python3
# def magic_string():
#     magic_string.n = 0
#     magic_string.n += 1
#     return "BestSchool, " * (magic_string.n - 1) + "BestSchool"
def magic_string():
    magic_string.count = getattr(magic_string, "count", 0)
    magic_string.count += 1
    return "".join(["BestSchool, "] * magic_string.count) + "BestSchool"
