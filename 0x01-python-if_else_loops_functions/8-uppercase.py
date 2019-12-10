#!/usr/bin/python3
def uppercase(str):
    for i in range (len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            j = chr(ord(str[i]) - 32)
        print('{}'.format(j), end='')
    print()
