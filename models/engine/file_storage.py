#!/usr/bin/python3
"""
    FileStorage Module: This module defines a class
    that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User

new_dict = {
    "BaseModel": BaseModel,
    "User": User
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

        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """ Serializes __objects to a JSON file """

        my_dict = FileStorage.__objects
        obj_dict = {}
        for obj in my_dict.keys():
            obj_dict[obj] = my_dict[obj].to_dict()
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes a JSON file to __objects 
            (only if the JSON file (__file_path) exists
        """ 
        try:
            with open(FileStorage.__file_path) as f:
                new_data = json.load(f)

                for val in new_data.values():
                    cls_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cls_name)(**val))            

        except Exception:
                pass
