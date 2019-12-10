#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 15 == 0:
            x = "FizzBuzz"
        elif number % 3 == 0:
            x = "Fizz"
        elif number % 5 == 0:
            x = "Buzz"
        else:
            x = number
        print("{} ".format(x), end='')
