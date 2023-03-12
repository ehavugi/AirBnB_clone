#!/usr/bin/python3
"""
Tests for Amenity class

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """
    Test cases for Amenity model
    """
    testCase = Amenity()

    def test_user_attr(self):
        """
        check if Amenity has
            name attr
        """
        new = {"name": str}
        for attr in new:
            self.assertTrue(hasattr(self.testCase, attr))
            self.assertIsInstance(getattr(self.testCase, attr), new[attr])
