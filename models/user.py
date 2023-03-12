#!/usr/bin/python3
"""
Defines User Class
   + Inherents BaseModel
   +  attributes
"""
from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """
    User
        attr:
            email : string - empty string
            password : string - empty string
            first_name : string - empty string
            last_name : string - empty string
    """
    email = ""
    password = ""
    last_name = ""
    first_name = ""

    def __init__(self, *args, **kwargs):
        """
            Initialization to help with deserialization

        """
        tf = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(kwargs[key], tf)
                elif key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            super().__init__()
