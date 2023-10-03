#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = -1 * (abs(number) % 10) if number < 0 else number % 10
message = "Last digit of "
if last_digit > 5:
    message += f"{number} is {last_digit} and is greater than 5"
elif last_digit != 0:
    message += f"{number} is {last_digit} and is less than 6 and not 0"
else:
    message += f"{number} is {last_digit} and is 0"
print(message)
