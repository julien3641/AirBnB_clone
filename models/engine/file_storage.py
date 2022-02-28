#!/usr/bin/python3
"""
This module defines the class FileStorage.
"""
import json
import os


class FileStorage:
    """
    This class defines the file storage.

    Attributes:
        - __file_path (str)
        - __ __object (dict)
    """
    __file_path = "file.json"
    __object = {}

    def all(self):
        """
        This method returns the dictionary __object.
        """
        return self.__object

    def new(self, obj):
        """
        This method sets in __objects the obj with key <obj class name>.id
        """
        return self.__object["{}.{}".format(obj.__class__.__name__, obj.id)]

    def save(self):
        """
        This method serializes __object to the JSON file.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            return f.write(json.dumps(self.__object))

    def reload(self):
        """
        This method deserializes the JSON file to __object.
        """
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                return json.loads(f.read())
