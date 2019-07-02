#!/usr/bin/python3
""" doctest unittest """
import unittest
import pep8
from models.base_model import BaseModel


class Testpep8(unittest.TestCase):
    """ test pep8 """
    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_base_model = "models/base_model.py"
        file_test_base_model = "tests/test_models/test_base_model.py"
        check = style.check_files([file_base_model, file_test_base_model])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBase(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ first set up """
        cls.ins = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ final statement """
        pass

    def setUp(self):
        """ first set up before test """
        pass

    def tearDown(self):
        """ final statement after test """
        pass

    def test_BaseModeldoc(self):
        """ test base model documentation """
        self.assertNotEqual(len(BaseModel.__doc__), 0)

    def test_BaseModelAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "id"), True)
        self.assertEqual(hasattr(self.ins, "created_at"), True)
        self.assertEqual(hasattr(self.ins, "updated_at"), True)


if __name__ == '__main__':
    unittest.main()