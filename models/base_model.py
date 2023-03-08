#!/usr/bin/python3
import uuid
from datetime import datetime

"""
Class BaseModel:
    v0:

"""


class BaseModel():
    """
    BaseModel --v0
    """
    def __init__(self):
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
        return "[{}] ({}) {}".format(self.id, self.id, self.__dict__)

    def save(self):
        """
        update update_at attribute to now
        """
        self.updated_at = datetime.now()
        return None

    def to_dict(self):
        """
        returns a dictionary contain key/values from __dict__

        """
        dictRepr = self.__dict__
        dictRepr['update_at'] = self.updated_at.isoformat()
        dictRepr['created_at'] = self.created_at.isoformat()
        return dictRepr
