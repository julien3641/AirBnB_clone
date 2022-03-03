import unittest
import uuid
from datetime import datetime

from models.base_model import BaseModel


class TestId(unittest.TestCase):

    def test_bm_id_str(self):
        """test id str"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_bm_id_uuid(self):
        """test id uuid"""
        bm = BaseModel()
        self.assertIsInstance(uuid.UUID(bm.id), uuid.UUID)

    def test_bm_unique_id(self):
        """test unique id"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_len_id(self):
        bm = BaseModel()
        self.assertEqual(len(bm.id), 36)

    def test_create_time(self):
        bm = BaseModel()
        self.assertEqual(type(bm.created_at), datetime)

    def test_type_update(self):
        bm = BaseModel()
        self.assertEqual(type(bm.updated_at), datetime)

    def test_update_time(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.updated_at)

if __name__ == '__main__':
    unittest.main()
