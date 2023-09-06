#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
output = "Last digit of {} is {}"

# check for number that's less than 0
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
# check for number greater than 5
if last_digit > 5:
    print(output.format(number, last_digit), "and is greater than 5")
# check for number less than 6 and not 0
elif last_digit < 6 and last_digit != 0:
    print(output.format(number, last_digit), "and is less than 6 but not 0")
else:
    print(output.format(number, last_digit), "and is 0")
