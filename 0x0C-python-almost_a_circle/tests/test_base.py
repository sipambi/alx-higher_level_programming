#!/usr/bin/python3
"""unittest for class Base"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for class Base"""

    def test_id(self):
        """Test for id functionality"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(98)
        self.assertEqual(b3.id, 98)
        b4 = Base(256)
        self.assertEqual(b4.id, 256)
        b5 = Base()
        self.assertEqual(b5.id, 3)
        b6 = Base(-98)
        self.assertEqual(b6.id, -98)
        b7 = Base(None)
        self.assertEqual(b7.id, 4)
        b8 = Base(4.4)
        self.assertEqual(b8.id, 4.4)

    def test_from_to_json_string(self):
        """Test to_json_string and from_json_string methods"""
        dict1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dict1])
        self.assertEqual(dict1, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(Base.from_json_string(json_dictionary)[0], dict1)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
