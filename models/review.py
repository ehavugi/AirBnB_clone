#!/usr/bin/python3
"""
Defines Review Class
   + Inherents BaseModel
   + Name attribute
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    State
        attr :
            place_id: string - empty string
            user_id : string - empty string
            text : string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
