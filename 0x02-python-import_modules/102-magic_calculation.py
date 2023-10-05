#!/usr/bin/python3
def magic_calculation(a, b):
    from calculator_1 import (
        add,
        sub,
    )

    if a < b:
        c = add(a, b)
        for i in range(4):
            c = add(c, i)
    else:
        c = sub(a, b)
        for i in range(4):
            c = sub(c, i)
    return callable


import dis

dis.dis(magic_calculation)
