#!/usr/bin/python3
""" defines a function to check a class """


def is_same_class(obj, a_class):
    """ performs check whether object is of a class """
    if type(obj) == a_class:
        return True
    return False
