#!/usr/bin/python3
"""
Defines City Class
   + Inherents BaseModel
   + name attribute
   + state_id
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City
        attr: name
        attr: state_id --> from State.id
    """
    name = ""
    state_id = ""
