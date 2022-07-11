#!/usr/bin/python3
"""Define class Rectangle which inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle model class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"Initialiser"""

        @property
        def width(self):
            """Getter"""
            return self._width

        @width.setter
        def width(self, value):
            """Setter"""
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Getter"""
            return self.__height

        @height.setter
            def height(self, value):
                """Setter"""
                if type(value) != int:
                    raise TypeError("height must be an integer")
                if value <= 0:
                    raise ValueError("height must be > 0")
                self.__height = value
