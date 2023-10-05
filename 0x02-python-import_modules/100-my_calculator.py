#!/usr/bin/python3
from calculator_1 import div, add, sub, mul
import argparse
from sys import argv, exit

operators = {"+": add, "-": sub, "*": mul, "/": div}
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator_found = False
        if argv[2] in operators:
            operator = argv[2]
            print(
                "{} {} {} = {}".format(
                    argv[1],
                    operator,
                    argv[3],
                    operators[operator](int(argv[1]), int(argv[3])),
                )
            )
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
