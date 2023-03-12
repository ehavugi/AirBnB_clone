#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
"""
tests for base model

"""


class TestUser(TestBaseModel):
    """
    Test cases for base model.
    """
    testCase = User()

    def test_user_attr(self):
        """
        check if user has
            "Email", first_name, password, last_name
        """
        new = {
             "email": str, "last_name": str,
             "first_name": str, "password": str
             }
        for attr in new:
            self.assertTrue(hasattr(self.testCase, attr))
            self.assertIsInstance(getattr(self.testCase, attr), new[attr])
