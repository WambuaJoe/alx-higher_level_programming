#!/usr/bin/python3
""" define class MyInt """


class MyInt(int):
    """ inversion of == & != """

    def __eq__(self, other):
        """ changes made to == """
        return int(self) != int(other)

    def __ne__(self, other):
        """ changes made to != """
        return int(self) == int(other)
