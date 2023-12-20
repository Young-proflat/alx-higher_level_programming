#!/usr/bin/python3
""" Defining a classes """


class Square:
    """ creating a class """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): The size of the square (default is 0).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
