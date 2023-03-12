#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

"""
Class BaseModel:
    v0:

"""


class BaseModel():
    """
    BaseModel --v0
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the model

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
        storage.new(self)
        storage.save()
        return None

    def to_dict(self):
        """
        returns a dictionary contain key/values from __dict__

        """
        dictRepr = self.__dict__.copy()
        dictRepr['updated_at'] = str(self.updated_at.isoformat())
        dictRepr['created_at'] = str(self.created_at.isoformat())
        dictRepr['__class__'] = str(self.__class__.__name__)
        return dictRepr
