#!/usr/bin/python3
"""
    Module containing a Function thet returns the JSON representationn of an object
"""
import json


def to_json_string(my_obj):
    """ Returns JSON rep of an obj
        Args:
            my_obj
    """
    return json.dumps(my_obj)
