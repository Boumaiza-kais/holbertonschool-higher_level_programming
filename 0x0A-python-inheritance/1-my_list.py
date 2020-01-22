#!/usr/bin/python3

'''
this module have Mylist class
'''


class MyList(list):
    '''
        prints the list, but sorted (ascending sort)
    '''
    def print_sorted(self):
        print(sorted(self))
