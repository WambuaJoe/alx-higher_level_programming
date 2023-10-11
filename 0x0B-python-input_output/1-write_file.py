#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):
    """write string to text file """

    with open(filename, 'w', encoding='UTF-8') as file:
        return file.write(text)
