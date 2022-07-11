#!/usr/bin/python3
"""Define class Square which inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square model class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides ___str___"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        if args:
            attributes = ["id", "size", "x", "y"]
            i = 0
            for v in args:
                setattr(self, attributes[i], v)
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns dict rep of instance"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
