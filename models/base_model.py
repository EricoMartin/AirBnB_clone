#!/usr/bin/python3
""" The BaseModel Module

    A BaseModel class that defines all common
    attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models 


class BaseModel:
    """
        BaseModel: A superclass that defines all
        common attributes/methods for other classes

        Private Class Attributes:
        __nb_object (int): number of object instances.
    """
    
    def __init__(self, *args, **kwargs):
        """
            Superclass Constructor initialization.
            This method instantiates every newly created object
        
            Args:
                *args: variable list of args
                **kwargs: variable list of keyworded args
                id (int): uuid of current instance
                created_at (datetime): The time current instance
                was created
                updated_at (datetime): The time current instance
                was updated
        """

        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

        if len(kwargs) != 0:
            tformat = "%Y-%m-%dT%H:%M:%S.%f" 
            for key, value in kwargs.items():
                if (key == "created_at"):
                    self.created_at = datetime.strptime(value, tformat)
                elif (key == "updated_at"):
                    self.updated_at = datetime.strptime(value, tformat)
                else:
                    setattr(self, key, value)

        else:
            models.storage.new(self)

    def __str__(self):
        """
            prints the string representation of the object instance
            print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            A function that saves the data to our database.
            it also updates the public instance attribute updated_at 
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        d_dict = self.__dict__.copy()
        d_dict["created_at"] = self.created_at.isoformat()
        d_dict["updated_at"] = self.updated_at.isoformat()
        d_dict["__class__"] = self.__class__.__name__

        return d_dict
