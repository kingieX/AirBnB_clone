#!/usr/bin/python3
'''
    this module contains the python storageclass
    this class serielizes instances to JSON and
    deserializes JSON file to instances
    '''

import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    '''
    serializes and deserializes
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
            returns __objects dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
            sets __objects
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
            serializes __objects to JSON
        '''
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        '''reloads from JSON file'''

        try:
            with open(FileStorage.__file_path, 'r') as f:
                my_dict = json.load(f)
                for key, obj_dict in my_dict.items():
                    for key in obj_dict.keys():
                        if key == "__class__":
                            cls_name = '' + obj_dict[key]
                    loaded_obj = eval(cls_name)(**obj_dict)
                    FileStorage.__objects[key] = loaded_obj
        except:
            pass
