#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """this class gather all test concerning place"""
    def test_cityId_type(self):
        """test the city id type from place file"""
        var = Place()
        self.assertIsInstance(var.city_id, str)

    def test_userId_type(self):
        """test the user id type from place file"""
        var = Place()
        self.assertIsInstance(var.user_id, str)

    def test_name_type(self):
        """test the name type from place file"""
        var = Place()
        self.assertIsInstance(var.name, str)

    def test_description_type(self):
        """test the description type from place file"""
        var = Place()
        self.assertIsInstance(var.description, str)

    def test_number_of_rooms_type(self):
        """test the number of rooms type from place file"""
        var = Place()
        self.assertIsInstance(var.number_rooms, int)

    def test_number_of_bathroom_type(self):
        """test the number of bathroom type from place file"""
        var = Place()
        self.assertIsInstance(var.number_bathrooms, int)

    def test_max_guest_type(self):
        """test the max guest type from place file"""
        var = Place()
        self.assertIsInstance(var.max_guest, int)

    def test_price_by_night_type(self):
        """test the price by night type from place file"""
        var = Place()
        self.assertIsInstance(var.price_by_night, int)

    def test_latitude_type(self):
        """test the latitude type from place file"""
        var = Place()
        self.assertIsInstance(var.latitude, float)

    def test_longitude_type(self):
        """test the longitude type from place file"""
        var = Place()
        self.assertIsInstance(var.longitude, float)

    def test_amenity_id_type(self):
        """test the longitude type from place file"""
        var = Place()
        self.assertIsInstance(var.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
