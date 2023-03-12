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

    def __init__(self, *args, **kwargs):
        """
        initialize State

        """
        super().__init__(*args, **kwargs)
