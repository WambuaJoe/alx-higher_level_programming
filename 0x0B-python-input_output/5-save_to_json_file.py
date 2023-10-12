#!/usr/bin/python3
""" json module """
import json


def save_to_json_file(my_obj, filename):
    """  write an Object to a text file, using
        JSON representation
    """
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(my_obj, file)
