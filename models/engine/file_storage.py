#!/usr/bin/python3
'''
    this module contains the python storageclass
    this class serielizes instances to JSON and
    deserializes JSON file to instances
    '''

import json
import os
import uuid
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
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        '''reloads from JSON file'''

        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                my_dict = json.load(f)
                for key, v in my_dict.items():
                    FileStorage.__objects[key] = eval(v['__class__'])(**v)
