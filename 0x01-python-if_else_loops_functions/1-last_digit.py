#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number % 10)
if number < 0:
    last_d = -last_d
print("Last digit of {} is {} and is ".format(number, last_d), end="")
if last_d > 5:
    print("greater than 5")
elif last_d == 0:
    print("0")
else:
    print("less than 6 and not 0")
