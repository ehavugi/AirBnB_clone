#!/usr/bin/python3
"""
Defines Amenity Class
   + Inherents BaseModel
   + Name attribute
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity
        attr: name
    """
    name = ""
