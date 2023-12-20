#!/usr/bin/python3
""" creating a class """
class Square:
    """ Initializing data """
    def __init__(self, size=0):
        """" sets the size to a value """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


