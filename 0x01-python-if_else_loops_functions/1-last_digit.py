#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number)
num1 = (num % 10)

if (number % 10) > 5:
    print(f"Last digit of {number} is {number % 10} and is greater than 5")
elif (number % 10) == 0:
    print(f"Last digit of {number} is {number % 10} and is 0")
elif number < 0:
    print(f"Last digit of {number} is {-num1} and is less \
than 6 and not 0")
elif (number % 10) < 6 and (number % 10) > 0:
    print(f"Last digit of {number} is {number % 10} and is less than 6 \
and not 0")
