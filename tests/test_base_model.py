#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_save(self):
        """Test saving a BaseModel instance"""
        bm = BaseModel()
        bm.save()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict(self):
        """Test converting a BaseModel instance to a dictionary"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)

    def test_from_dict(self):
        """Test creating a BaseModel instance from a dictionary"""
        data = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            '__class__': 'BaseModel'
        }
        bm = BaseModel(**data)
        self.assertEqual(bm.id, data['id'])
        self.assertEqual(bm.created_at.isoformat(), data['created_at'])
        self.assertEqual(bm.updated_at.isoformat(), data['updated_at'])
        self.assertEqual(type(bm.created_at), datetime)
        self.assertEqual(type(bm.updated_at), datetime)
        self.assertEqual(bm.__class__.__name__, 'BaseModel')

    def test_save_reload(self):
        """Test saving and reloading a BaseModel instance from storage"""
        bm = BaseModel()
        bm.save()
        bm_id = bm.id

        # Create a new instance and reload data from storage
        bm_new = BaseModel()
        storage.reload()

        # Check if the new instance matches the reloaded data
        self.assertEqual(bm_new.id, bm_id)
        self.assertEqual(bm_new.created_at, bm.created_at)
        self.assertEqual(bm_new.updated_at, bm.updated_at)

    def test_str(self):
        """Test string representation of a BaseModel instance"""
        bm = BaseModel()
        bm_str = str(bm)
        self.assertEqual(bm_str, "[BaseModel] ({}) {}".format(bm.id, bm.__dict__))


if __name__ == '__main__':
    unittest.main()
