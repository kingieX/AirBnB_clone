#!/usr/bin/python3
'''defines unittests for our project'''


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    '''tests the instantiation of BaseModel'''

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_date_time_obj(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_date_time_obj(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_unique_ids(self):
        b = BaseModel()
        d = BaseModel()
        self.assertNotEqual(b.id, d.id)

    def test_two_different_updated_at(self):
        b1 = BaseModel()
        sleep(0.1)
        b2 = BaseModel()
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test__str_rep(self):
        b = BaseModel()
        b.id = "22222"
        dict_str = str(b.__dict__)
        string = "[BaseModel] (22222) " + dict_str
        self.assertEqual(string, b.__str__())

    def test_unused_arg(self):
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_instantiation_wit_kwargs(self):
        dt = datetime.now()
        dt_s = dt.isoformat()
        b = BaseModel(id='343', created_at=dt_s, updated_at=dt_s)
        self.assertEqual(b.id, '343')
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.now()
        dt_s = dt.isoformat()
        b = BaseModel('50', id='343', created_at=dt_s, updated_at=dt_s)
        self.assertNotIn('50', b.__dict__.values())
        self.assertEqual(b.id, '343')
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

class test_BaseModel_save(unittest.TestCase):
    '''tests the save method of BaseModel'''

    @classmethod
    def Setup(self):
        try:
            os.rename('file.json', 'temp')
        except IOError:
            pass

    @classmethod
    def Teardown(self):
        try:
            os.remove('file.json')
        except IOError:
            pass
        try:
            os.rename('temp', 'file.json')
        except IOError:
            pass

    def test_first_save(self):
        b = BaseModel()
        test_updated_at = b.updated_at
        sleep(0.1)
        b.save()
        self.assertLess(test_updated_at, b.updated_at)

    def test_two_save(self):
        b = BaseModel()
        test_first_updated_at = b.updated_at
        sleep(0.05)
        b.save()
        test_second = b.updated_at
        sleep(0.05)
        b.save()
        self.assertLess(test_second, b.updated_at)

    def test_save_with_arg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.save(None)

    def test_save_updates_file(self):
        b = BaseModel()
        b.save()
        key = 'BaseModel.' + b.id
        with open('file.json', 'r') as f:
            self.assertIn(key, f.read())

class Test_BaseModel_to_dict(unittest.TestCase):
    '''tests the to_dict method of BaseModel'''

    def test_to_dict_type(self):
        b = BaseModel()
        self.assertEqual(dict, type(b.to_dict()))

    def test_if_contains_correct_keys(self):
        b = BaseModel()
        self.assertIn('id', b.to_dict())
        self.assertIn('created_at', b.to_dict())
        self.assertIn('updated_at', b.to_dict())
        self.assertIn('__class__', b.to_dict())

    def test_to_dict_contains_added_attributes(self):
        b = BaseModel()
        b.name = 'Stephen'
        b.Age = 50
        self.assertIn('name', b.to_dict())
        self.assertIn('Age', b.to_dict())

    def test_to_dict_datetime_attr_are_str(self):
        b = BaseModel()
        m_dict = b.to_dict()
        self.assertEqual(str, type(m_dict['updated_at']))
        self.assertEqual(str, type(m_dict['created_at']))

    def test_diff_to_dict_and_dunder_dict(self):
        b = BaseModel()
        self.assertNotEqual(b.to_dict(), b.__dict__)

    def test_to_dict_with_arg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(None)

    def test_to_dict_output(self):
        d = datetime.now()
        b = BaseModel()
        b.id = '222'
        b.updated_at = b.created_at = d
        m_dict = {
            'id': '222',
            '__class__': 'BaseModel',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(b.to_dict(), m_dict)



if __name__ == '__main__':
    unittest.main()
