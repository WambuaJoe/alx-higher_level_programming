#!/usr/bin/python3
""" Base module """
import json


class Base:
    """ create Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiate Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation
            to a file
        """
        file = str(cls.__name__) + ".json"
        dict_list = []
        if list_objs is None:
            new_file.write(dict_list)
        else:
            with open(file, "w", encoding="utf-8") as new_file:
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                new_file.write(cls.to_json_string(dict_list))
