#!/usr/bin/python3
"""
module for class_to_json method
"""


def class_to_json(obj):
    """
    returns dict description for json
    serialization of object
    Args:
        obj: object to be serialized
    """
    return obj.__dict__
