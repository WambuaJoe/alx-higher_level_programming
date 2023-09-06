#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
output = "Last digit of {} is {}"

for i in range(0, number):
    last_digit = i % 10
    if last_digit < 6 and last_digit != 0:
        print(output.format(number, last_digit)
              + " and is less than 6 and not 0")
    elif last_digit > 5:
        print(output.format(number, last_digit) + " and is greater than 5")
    elif last_digit == 0:
        print(output.format(number, last_digit) + " and is 0")
