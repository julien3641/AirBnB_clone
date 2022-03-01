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
    __objects = {}

    def all(self):
        """
        This method returns the dictionary __object.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        This method sets in __objects the obj with key <obj class name>.id
        """
        key_class = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key_class, obj.id)] = obj

    def save(self):
        """
        This method serializes __object to the JSON file.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)
"""
    def reload(self):
        
        This method deserializes the JSON file to __object.
     
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
"""