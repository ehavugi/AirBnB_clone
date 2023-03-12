#!/usr/bin/python3
"""
FileStorage module.
    + database based on json
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """
    File storage
        methods
            + all -- returns dictionary __objects
            + new -- sets new  object in __objects
            + save -- save json to file
            + reload -- load json from file into __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return all objects in storage.

        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
            key <obj class name>.id
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)

        self.__objects[key] = obj

    def save(self):
        """
            write to a json file
        """
        all_dict = self.__objects
        objects_dict = {key: all_dict[key].to_dict() for key in all_dict}
        with open(self.__file_path, "w") as out:
            json.dump(objects_dict, out)

    def reload(self):
        """
        Load the objects from a json file.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                for key in objects:
                    class_name = objects[key]["__class__"]
                    del objects[key]["__class__"]
                    self.new(eval(class_name)(**objects[key]))
