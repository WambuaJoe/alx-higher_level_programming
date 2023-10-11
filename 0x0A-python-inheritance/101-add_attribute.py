#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, attr_name, value):
    """ add new attribute to an object if allowed
        Args:
            obj: object whose value is to be set
            attr_name: attribute name for which value
                       is to be set
            value: attribute value to be set
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
