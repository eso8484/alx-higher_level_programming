#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num = number % 10
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    if num == 0:
        print(f"Last digit of {number} is {num} and is 0")
    if num < 6 and num != 0:
        print(f"last digit of {number} is {num} and is less than 6 and not 0")
else:
    numbe = number * -1
    num = numbe % 10
    num = -1 * num
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    if num == 0:
        print(f"Last digit of {number} is {num} and is 0")
    if num < 6 and num != 0:
        print(f"last digit of {number} is {num} and is less than 6 and not 0")
