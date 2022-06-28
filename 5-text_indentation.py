#!/usr/bin/python3
"""
Defines a text-indentation function.
Module test_indentation
Prints a text with 2 new lines after each of these character.
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
