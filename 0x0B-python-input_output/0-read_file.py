#!/usr/bin/python3
"""
    Module containing a file reading function
"""


def read_file(filename=""):
    """ Function that reads from a file
        Args:
            filename: filename
    """
    with open(filename, encoding = "utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
