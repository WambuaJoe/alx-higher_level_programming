#!/usr/bin/python
def uppercase(str):
    """ print string in uppercase """
    for char in str:
        if 123 > ord(char) >= 97:
            char = chr(ord(char) - 32)
        print("{}".format(char), end='')
    print()
