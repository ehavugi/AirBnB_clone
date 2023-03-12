#!/usr/bin/python3
"""
Units tests for Review Class

"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """
    Test cases for Review
    """
    testCase = Review()

    def test_review_attr(self):
        """
        check if review has
            place_id, user_id, text
        """
        new = {
             "place_id": str, "user_id": str,
             "text": str
             }
        for attr in new:
            self.assertTrue(hasattr(self.testCase, attr))
            self.assertIsInstance(getattr(self.testCase, attr), new[attr])
