#!/usr/bin/python3
def roman_to_int(roman_string: str):
    mapping = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    if not roman_string:
        return 0
    if not isinstance(roman_string):
        return 0
    integer = 0
    for i in range(len(roman_string)):
        if (
            i < len(roman_string) - 1
            and mapping[roman_string[i]] < mapping[roman_string[i + 1]]
        ):
            integer -= mapping[roman_string[i]]
        else:
            integer += mapping[roman_string[i]]

    return integer
