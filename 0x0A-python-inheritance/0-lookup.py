#!/usr/bin/python3
""" 0-lookup module """


def lookup(obj):
    """ function returns list of available attributes
        and methods of an object
        Args:
            obj: object to be inspected
        Returns:
            list: list of available attributes & methods
    """
    return dir(obj)
