#!/usr/bin/python3
"""
    Module containing a file writing function
"""


def append_write(filename="", text=""):
    """ Function that appends and write to a file
        Args:
            filename: filename
            text: text to be written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
