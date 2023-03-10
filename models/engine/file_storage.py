#!/usr/bin/python3
import json


class FileStorage():
    """
    File storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return all objects in storage
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)

        self.__objects[key] = obj.to_dict()

    def save(self):
        """
            write to a json file
        """
        json_obj = json.dumps(self.__objects)
        with open(self.__file_path, "w") as out:
            out.write(json_obj)

    def reload(self):
        """
        Load the objects from a json file


        """
        with open(self.__file_path, "r") as f:
            self.__objects = json.load(f)
