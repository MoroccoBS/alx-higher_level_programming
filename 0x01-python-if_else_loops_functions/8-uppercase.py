#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii = ord(char)
        uppercase_ascii = ascii - 32 if 97 <= ascii <= 122 else ascii
        print("{:c}".format(chr(uppercase_ascii)), end="")
    print()
