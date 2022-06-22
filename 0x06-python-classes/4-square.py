#!/usr/bin/python3
""" class square with size defined by prev task"""


class Square:
    """ the class sqaure"""

    def __init__(self, size=0):
        """ to construct the square with size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """ method to get area of the shape(square)"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter to the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter to the private attribute size"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
