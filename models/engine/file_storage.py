#!/usr/bin/python3
"""
    FileStorage Module: This module defines a class
    that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel

new_dict = {
    "BaseModel": BaseModel
    }


class FileStorage:
    """FileStorage class declaration"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This function returns the dictionary
        of all objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
    
        Args:
            obj: The current object to get its id
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to a JSON file """

        my_list = {}
        for obj in FileStorage.__objects.keys():
            new_obj = FileStorage.__objects[obj].to_dict()
            my_list.update(new_obj)
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(my_list, file)

    def reload(self):
        """ deserializes a JSON file to __objects 
            (only if the JSON file (__file_path) exists
        """ 
        try:
            with open(FileStorage.__file_path, "r") as file:
                new_data = json.load(file)

                for val in new_data.values():
                    del val['__class__']
                    self.new(eval[val['__class__']](**val))            

        except Exception:
                pass
