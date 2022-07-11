#!/usr/bin/python3
"""Define class Base"""
import json


class Base:
    """Base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialiser"""
        if id is not None:
            self.id = id
        else
            __nb_objects =+ 1
            self.id = Base.__nb_objects

