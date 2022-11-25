#!/usr/bin/python3
'''
    this module contains the basemodel class
    '''


import uuid
from datetime import datetime
import models


class BaseModel:
    '''
        class of type BaseModel
        '''

    def __init__(self, *args, **kwargs):
        '''
            initializes class object
            from dictionary
            '''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
            creates a user-friendly string display of object
                '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
            updates update_at with current datetime
                '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
            returns dict of __dict__ of class instance
            '''
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
