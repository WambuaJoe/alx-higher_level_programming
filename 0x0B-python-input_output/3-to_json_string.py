#!/usr/bin/python3
""" json module """
import json


def to_json_string(my_obj):
    """  returns the JSON representation of an object """
    return json.dumps(my_obj)
