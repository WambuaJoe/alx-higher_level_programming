#!/usr/bin/python3
""" json module """
import json


def from_json_string(my_str):
    """  returns an object represented by a JSON string """
    return json.loads(my_str)
