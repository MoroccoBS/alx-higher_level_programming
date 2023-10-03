#!/usr/bin/python3
for number in range(100):
    if number != 100 - 1:
        print("{:02d}".format(number), end=", ")
    else:
        print(
            "{:02d}".format(number),
        )
