#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """ inherits from list """
    def __init__(self):
        """ initiates MyList class """
        super().__init__()
    
    def print_sorted(self):
        """ prints list in ascending order """
        print(sorted(self))
