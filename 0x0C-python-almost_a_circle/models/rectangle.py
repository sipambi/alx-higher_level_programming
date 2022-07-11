#!/usr/bin/python3
"""Define class Rectangle which inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle model class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter"""
        return self.__width

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

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of instance"""
        return self.width * self.height

    def display(self):
        """Print visual representation of instance"""
        if self.width == 0 or self.height == 0:
            print("")
        row = (' ' * self.x) + ('#' * self.width) + '\n'
        print(('\n' * self.y) + row * (self.height - 1) + (
            (' ' * self.x) + ('#' * self.width)))

    def __str__(self):
        """Overrides ___str___"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            i = 0
            for v in args:
                setattr(self, attributes[i], v)
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns dict rep of instance"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
