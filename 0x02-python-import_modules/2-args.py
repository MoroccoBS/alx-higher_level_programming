#!/usr/bin/python3
import sys

argv = sys.argv
numberOfArgv = len(argv) - 1
text = "arguments:" if numberOfArgv > 0 else "arguments."
print("{:d} {:s}".format(numberOfArgv, text))

for index in range(numberOfArgv):
    print("{:d}: {:s}".format(index + 1, argv[index + 1]))
