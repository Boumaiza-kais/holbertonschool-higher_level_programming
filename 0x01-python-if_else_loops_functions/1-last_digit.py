#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = ("Last digit of")
if number >= 0:
    x = number % 10
if number < 0:
    x = number % -10
if x > 5:
    print("{} {} is {} and is greater than 5".format(l, number, x))
elif x == 0:
    print("{} {} is {} and is 0".format(l, number, x))
else:
    print("{} {} is {} and is less than 6 and not 0".format(l, number, x))
