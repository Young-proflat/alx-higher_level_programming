#!/usr/bin/python3
""" creating a class """
class Square:
    """ Initializing data """
    def __init__(self, size=0):
        self.__size = size
     """Sets the size to a value."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = value


