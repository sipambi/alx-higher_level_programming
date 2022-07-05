#!/usr/bin/python3
"""
    Module containing a file writing function
"""


def write_file(filename="", text=""):
    """ Function that write to a file
        Args:
            filename: filename
            text: text to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
