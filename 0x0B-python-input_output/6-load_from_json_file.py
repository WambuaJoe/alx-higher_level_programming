#!/usr/bin/python3
""" json module """
import json


def load_from_json_file(filename):
    """ create object from JSON file """
    with open(filename, mode='r') as json_file:
        return json.load(json_file)
