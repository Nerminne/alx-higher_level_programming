#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    posNum = number * -1
    last = (posNum % 10) * -1
else:
    posNum = number
    last = posNum % 10
if (last > 5):
    string = "and is greater than 5"
elif (last == 0):
    string = "and is 0"
else:
    string = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {string}")
