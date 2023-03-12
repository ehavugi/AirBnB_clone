#!/usr/bin/python3

"""
Unit tests for Place model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """
    Test cases for Place model
    """
    testCase = Place()

    def test_place_attr(self):
        """
        check if place has
            city_id, user_id, name
            description, number_rooms
            number_bathrooms,max_guest
            price_by_night, latitude,
            longitude,
            amenity_ids
        """
        new = {
                "city_id": str, "user_id": str,
                "name": str, "description": str,
                "number_rooms": int, "number_bathrooms": int,
                "max_guest": int, "price_by_night": int,
                "latitude": float, "longitude": float,
                "amenity_ids": list
                }
        for attr in new:
            self.assertTrue(hasattr(self.testCase, attr))
            self.assertIsInstance(getattr(self.testCase, attr), new[attr])
