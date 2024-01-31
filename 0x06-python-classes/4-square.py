#!?usr/bin/python3 
""" creating a classes """
class Square:
    def __init__(self, size):
        self.__size = size
@getter
    def size(self):
        """self setter"""
    return self.__size
@setter    
    def size(self, value):
        if type(value) is not int:
            raise TypeError('sie must be an integer')
        if size > 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size ** 2

