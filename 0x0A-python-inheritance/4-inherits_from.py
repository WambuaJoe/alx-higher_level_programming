#!/usr/bin/python3
""" defines a function to compare classes """


def inherits_from(obj, a_class):
    """
    performs a check to assess whether an object is an
    instance of a class that (directly/indirectly)
    inherited from the specified class
    Args:
        obj: object
        a_class: class object
    Returns:
        True or False
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
