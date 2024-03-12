#!/usr/bin/python3
"""
Test script for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a BaseModel instance for testing.
        """
        self.model = BaseModel()

    def test_init_no_args(self):
        """
        Test the initialization of BaseModel
        without arguments.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_init_with_args(self):
        """
        Test the initialization of BaseModel with arguments.
        """
        data = {
            'id': 'test_id',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-02T00:00:00.000000'
        }
        model_with_args = BaseModel(**data)

        self.assertEqual(model_with_args.id, data['id'])
        self.assertEqual(model_with_args.created_at,
                         datetime.strptime(data['created_at'],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model_with_args.updated_at,
                         datetime.strptime(data['updated_at'],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_save_method(self):
        """
        Test the save method of BaseModel.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel.
        """
        expected_dict = {
            'id': self.model.id,
            'created_at': self.model.created_at.isoformat(),
            'updated_at': self.model.updated_at.isoformat(),
            '__class__': self.model.__class__.__name__
        }
        self.assertEqual(self.model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
