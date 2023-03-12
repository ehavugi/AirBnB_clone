#!/usr/bin/python3
"""
Class BaseModel.
    attributes
        id
        updated_at
        created_at
    methods
        __str__
        save
        to_dict


"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BaseModel --v0
       attributes: id, created_at, updated_at

    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the model
            args: not used
            kwargs: checked and used to updated __dict__
        """
        tf = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(kwargs[key], tf)
                elif key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            time_now = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = time_now
            self.updated_at = time_now
            models.storage.new(self)

    def __str__(self):
        """
        str representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        update update_at attribute to now
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary contain key/values from __dict__

        """
        dictRepr = self.__dict__.copy()
        dictRepr['updated_at'] = str(self.updated_at.isoformat())
        dictRepr['created_at'] = str(self.created_at.isoformat())
        dictRepr['__class__'] = str(self.__class__.__name__)
        return dictRepr
