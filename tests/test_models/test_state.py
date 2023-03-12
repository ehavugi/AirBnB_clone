#!/usr/bin/python3
"""
Tests for State

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """
    Test cases for base model.
    """
    testCase = State()

    def test_State_attr(self):
        """
        check if state has
            "name"
        """
        new = {"name": str}
        for attr in new:
            self.assertTrue(hasattr(self.testCase, attr))
            self.assertIsInstance(getattr(self.testCase, attr), new[attr])
