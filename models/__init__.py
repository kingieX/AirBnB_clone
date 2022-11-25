#!/usr/bin/python3
'''
    module to create unique filestorage instance
    '''


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
