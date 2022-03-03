#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """this class gather all test concerning amenety"""
    def test_name_type(self):
        """test name type from amenity file"""
        var = Amenity()
        self.assertIsInstance(var.name, str)


if __name__ == '__main__':
    unittest.main()
