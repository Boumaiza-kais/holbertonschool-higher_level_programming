#!/usr/bin/python3
'''
This module contain the class Base
'''

import json


class Base:
    '''
    class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''instansiation of the base'''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''to_jason_string fun'''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save_to_file fun'''
        l = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                l.append(i.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        '''from_jason_string fun'''

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create function'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
