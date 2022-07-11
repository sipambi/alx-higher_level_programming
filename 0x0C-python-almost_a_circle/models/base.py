#!/usr/bin/python3
"""Define class Base"""
import json


class Base:
    """Base class for other classes. Manages id attribute in
    all future classes and avoids duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string rep from list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves to JSON file"""
        dictionaries = [obj.to_dictionary() for obj in list_objs] \
            if list_objs is not None else []
        with open(cls.__name__ + ".json", 'w') as file:
            file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns list from JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates new object from dictionary list"""
        new = cls(1, 1, 0, 0) if cls.__name__ == "Rectangle" else cls(1, 0, 0)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Loads instance objects from JSON file"""
        try:
            with open(cls.__name__ + ".json") as file:
                return [cls.create(**objs) for objs in cls.from_json_string(
                    file.read())]
        except Exception:
            return []
