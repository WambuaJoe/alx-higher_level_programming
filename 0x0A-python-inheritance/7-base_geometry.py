#!/usr/bin/python3
""" defines a class BaseGeometry """


class BaseGeometry:
        """ represents BaseGeometry """
        def area(self):
            """ raises an exception """
            raise Exception("area() has not been implemented")

        def integer_validator(self, name, value):
            """ checks the value """
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than zero".format(name))
