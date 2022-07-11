#!/usr/bin/python3
"""unittest for class Square"""
import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for class Square"""

    def test_attributes(self):
        """Test attribute initialization"""
        s1 = Square(98, 99, 100, 101)
        self.assertEqual(s1.size, 98)
        self.assertEqual(s1.x, 99)
        self.assertEqual(s1.y, 100)
        self.assertEqual(s1.id, 101)

    def test__str__(self):
        """Test __str__ method"""
        s1 = Square(98, 128, 256, 1024)
        self.assertEqual(s1.__str__(), "[Square] (1024) 128/256 - 98")

    def test_update(self):
        """Test update method"""
        s1 = Square(1, 1, 1, 1)
        s1.update(98, 128, 256, 1024)
        self.assertEqual(s1.id, 98)
        self.assertEqual(s1.size, 128)
        self.assertEqual(s1.x, 256)
        self.assertEqual(s1.y, 1024)
        s2 = Square(1, 1, 1, 1)
        s2.update(id=98, size=128, x=256, y=1024)
        self.assertEqual(s2.id, 98)
        self.assertEqual(s2.size, 128)
        self.assertEqual(s2.x, 256)
        self.assertEqual(s2.y, 1024)

    def test_typeError(self):
        """Test typeError raises"""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(None)
        with self.assertRaises(TypeError):
            Square("Holberton")
        with self.assertRaises(TypeError):
            Square("Holberton", 29)
        with self.assertRaises(TypeError):
            Square(98, 128, "Holberton")

    def test_valueError(self):
        """Test valueError raises"""
        with self.assertRaises(ValueError):
            Square(0, 98, 128, 256)
        with self.assertRaises(ValueError):
            Square(98, -1, -4, 128)
        with self.assertRaises(ValueError):
            Square(98, 128, -4, 256)
        with self.assertRaises(ValueError):
            Square(-98, 128, 256, 512)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(2, 4, 5, 6)
        self.assertEqual(s1.to_dictionary(), {"id": 6, "size": 2,
                                              "x": 4, "y": 5})

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
