#!/usr/bin/python3
"""
Unit tests for City class.

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """
    Test cases for base model
    """
    testCase = City()

    def test_user_attr(self):
        """
        check if City has
            state_id, name
        """
        new = {"state_id": str, "name": str}
        for attr in new:
            self.assertTrue(hasattr(self.testCase, attr))
            self.assertIsInstance(getattr(self.testCase, attr), new[attr])
