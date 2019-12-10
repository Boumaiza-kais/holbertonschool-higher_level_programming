#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            j = ord(i) - 32
        else:
            j = ord(i)
        print("{:c}".format(j), end="")
    else:
        print()
