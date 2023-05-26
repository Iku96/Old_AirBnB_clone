#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test fixture. Create an instance of BaseModel.
        """
        self.model = BaseModel()

        def test_id_is_unique_string(self):
            """
            Test that the id attribute is a unique string.
            """
            self.assertIsInstance(self.model.id, str)
            self.assertNotEqual(self.mode.id, '')

        def test_created_at_is_datetime(self):
            """
            Test that the created_at attribute is a datetime object.
            """
            self.assertIsInstance(self.model.created_at, datetime)
        
        def test_updated_at_is_datetime(self):
            """
            Test that the updated_at attribute is a datetime object.
            """
            self.assertIsInstance(self.model.updated_at, datetime)

        def test_str_method(self):
            """
            Test the __str__ method of BaseModel.
            """
            expected_output = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
            self.assertEqual(str(self.model), expected_output)
        def test_save_updates_updated_at(self):
            """
            Test that the save method updates the updates_at attribute.
            """
            old_updated_at = seld.model.updated_at
            self.model.save()
            self.assertNotEqual(self.model.updated_at, old_updated_at)

            def test_to_dict_returns_dictionary(self):
                """
                Test that the to_dict method returns a dictionary.
                """
                obj_dict = self.model.to.dict()
                self.assertIsInstance(obj_dict, dict)

            def test_to_dict_contains_correct_keys(self):
                """
                Test that the to_dict method contains the correct keys.
                """
                expected_keys = ['id', 'created_at', 'updated_at, '__class__]
                obj.dict = self.model.to_dict()
                self.assertCountEqual(obj_dict.keys(), expected_keys)

            def test_to_dict_id_is_string(self):
                """
                Test that the 'id' key in the to_dict method is a string.
                """
                obj_dict = self.model.to_dict()
                self.assertIsInstance(obj_dict['id'], str)

            def test_to_dict_created_at_is_string_in_iso_format(self):
                """
                Test that the 'created_at' key in the to_dict method is a string in ISO format.
                """
                obj_dict = self.model.to_dict()
                self.assertIsInstance(obj_dict['created_at'], str)
                self.assertEqual(datetime.fromisoformat(obj_dict['created_at']), self.model.created_at)
            def test_to_dict_updated_at_is_string_in_iso_format(self):
        """
        Test that the 'updated_at' key in the to_dict method is a string in ISO format.
        """
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(datetime.fromisoformat(obj_dict['updated_at']), self.model.updated_at)

    def test_to_dict_class_name_is_base_model(self):
        """
        Test that the '__class__' key in the to_dict method is set to 'BaseModel'.
        """
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
