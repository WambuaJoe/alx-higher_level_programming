#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):
    """ append string at the end of a text file """

    with open(filename, 'a+', encoding='UTF-8') as file:
        file.write(text)
