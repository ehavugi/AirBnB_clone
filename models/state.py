#!/usr/bin/python3
"""
Defines State Class
   + Inherents BaseModel
   + Name attribute
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State
        attr: name
    """
    name = ""
