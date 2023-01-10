#!/usr/bin/python3
""" Defines MyList class """


class MyList(list):
    """ Initiate the class """

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
