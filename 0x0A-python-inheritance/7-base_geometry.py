#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """ raise an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value data type """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
