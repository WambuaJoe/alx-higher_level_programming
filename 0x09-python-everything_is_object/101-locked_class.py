#!/usr/bin/python3
""" LockedClass module """


class LockedClass:
    """ prevent user from dynamically creating new instance
        attributes, except if the new instance is first_name
    """
    __slots__ = ['first_name']
