#!/usr/bin/python3
"""
student class module
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """ initialize attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieve dict representation of student instance

        Returns:
            dict: dictionary representation
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, val in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = val
            return new_dict
