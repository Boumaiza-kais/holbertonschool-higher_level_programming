#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
             print("{:d}" .format(i), end="")
             count += 1
        except IndexError:
            return None
    print(end="\n")
    return count
