#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """ read text file & print to stdout
        Args:
            filename: name of file to be read from
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read(), end='')
