#!/usr/bin/python3
"""unittest for class Rectangle"""
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for class Rectangle"""

    def test_attributes(self):
        """Test attribute initialization"""
        r1 = Rectangle(98, 99, 100, 101, 102)
        self.assertEqual(r1.width, 98)
        self.assertEqual(r1.height, 99)
        self.assertEqual(r1.x, 100)
        self.assertEqual(r1.y, 101)
        self.assertEqual(r1.id, 102)
        r2 = Rectangle(98, 256)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 256)

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
        r2 = Rectangle(98, 256)
        self.assertEqual(r2.area(), 25088)

    def test__str__(self):
        """Test __str__ method"""
        r1 = Rectangle(98, 128, 256, 1024, 2048)
        self.assertEqual(r1.__str__(), "[Rectangle] (2048) 256/1024 - 98/128")

    def test_update(self):
        """Test update method"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(98, 128, 256, 1024, 2048)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 128)
        self.assertEqual(r1.height, 256)
        self.assertEqual(r1.x, 1024)
        self.assertEqual(r1.y, 2048)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(2, 4, 5, 6, 9)
        self.assertEqual(r1.to_dictionary(), {"id": 9, "width": 2,
                                              "height": 4, "x": 5, "y": 6})

    def test_typeError(self):
        """Test typeError raises"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(98)
        with self.assertRaises(TypeError):
            Rectangle(-98)
        with self.assertRaises(TypeError):
            Rectangle(None)
        with self.assertRaises(TypeError):
            Rectangle("Holberton")
        with self.assertRaises(TypeError):
            Rectangle("Holberton", 29)
        with self.assertRaises(TypeError):
            Rectangle(98, 128, "Holberton", 256)

    def test_valueError(self):
        """Test valueError raises"""
        with self.assertRaises(ValueError):
            Rectangle(0, 98, 128, 256, 512)
        with self.assertRaises(ValueError):
            Rectangle(98, -1, -4, 128, 256)
        with self.assertRaises(ValueError):
            Rectangle(98, 128, -4, 256, 512)
        with self.assertRaises(ValueError):
            Rectangle(-98, 128, 256, 512, 1024)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()#!/usr/bin/python3
"""unittest for class Rectangle"""
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for class Rectangle"""

    def test_attributes(self):
        """Test attribute initialization"""
        r1 = Rectangle(98, 99, 100, 101, 102)
        self.assertEqual(r1.width, 98)
        self.assertEqual(r1.height, 99)
        self.assertEqual(r1.x, 100)
        self.assertEqual(r1.y, 101)
        self.assertEqual(r1.id, 102)
        r2 = Rectangle(98, 256)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 256)

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
        r2 = Rectangle(98, 256)
        self.assertEqual(r2.area(), 25088)

    def test__str__(self):
        """Test __str__ method"""
        r1 = Rectangle(98, 128, 256, 1024, 2048)
        self.assertEqual(r1.__str__(), "[Rectangle] (2048) 256/1024 - 98/128")

    def test_update(self):
        """Test update method"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(98, 128, 256, 1024, 2048)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 128)
        self.assertEqual(r1.height, 256)
        self.assertEqual(r1.x, 1024)
        self.assertEqual(r1.y, 2048)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(2, 4, 5, 6, 9)
        self.assertEqual(r1.to_dictionary(), {"id": 9, "width": 2,
                                              "height": 4, "x": 5, "y": 6})

    def test_typeError(self):
        """Test typeError raises"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(98)
        with self.assertRaises(TypeError):
            Rectangle(-98)
        with self.assertRaises(TypeError):
            Rectangle(None)
        with self.assertRaises(TypeError):
            Rectangle("Holberton")
        with self.assertRaises(TypeError):
            Rectangle("Holberton", 29)
        with self.assertRaises(TypeError):
            Rectangle(98, 128, "Holberton", 256)

    def test_valueError(self):
        """Test valueError raises"""
        with self.assertRaises(ValueError):
            Rectangle(0, 98, 128, 256, 512)
        with self.assertRaises(ValueError):
            Rectangle(98, -1, -4, 128, 256)
        with self.assertRaises(ValueError):
            Rectangle(98, 128, -4, 256, 512)
        with self.assertRaises(ValueError):
            Rectangle(-98, 128, 256, 512, 1024)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
