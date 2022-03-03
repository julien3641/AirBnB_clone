import unittest
import uuid

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


if __name__ == '__main__':
    unittest.main()
