#!/usr/bin/python3
import unittest
from models.review import Review


class TestState(unittest.TestCase):
    """this class gather all test concerning review"""
    def test_placeId_type(self):
        """test place id type from review file"""
        var = Review()
        self.assertIsInstance(var.place_id, str)

    def test_userId_type(self):
        """test user id type from review file"""
        var = Review()
        self.assertIsInstance(var.user_id, str)

    def test_text_type(self):
        """test text type from review file"""
        var = Review()
        self.assertIsInstance(var.text, str)


if __name__ == '__main__':
    unittest.main()
