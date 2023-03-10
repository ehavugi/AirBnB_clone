#!/usr/bin/python3
"""
Defines User Class
   + Inherents BaseModel
   +  attributes
"""
from models.base_model import BaseModel


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
