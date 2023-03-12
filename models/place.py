#!/usr/bin/python3
"""
Defines Place Class
   + Inherents BaseModel
   + Name attribute
"""
from models.base_model import BaseModel
from datetime import datetime


class Place(BaseModel):
    """
    Place
        attr:
            name : string - empty string
            city_id : string - empty string
            user_id : string - empty string
            name : string - empty string
            description : string - empty string
            number_rooms: integer - 0
            number_bathrooms: integer - 0
            max_guest : integer - 0
            price_by_night : integer -0
            latitude : float 0.0
            longitude : float 0.0
            amenity_ids : list of string - empty list
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initialze the values for place model
            args: not used
            kwargs: checked and used to update __dict__
        """
        tf = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key in kwargs:
                if key in ['created_at', "updated_at"]:
                    self.__dict__[key] = datetime.strptime(kwargs[key], tf)
                elif key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            super().__init__(*args, **kwargs)
