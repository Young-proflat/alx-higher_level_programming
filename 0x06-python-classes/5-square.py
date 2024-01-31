#!/usr/bin/python3
""" classes in size """
class square:
    
    def __init__(self, size=0):
    """ initializing the size class """
        self.__size = size
@getter
    def size(self):
        return self.__size
@setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be am integer')
        if size > 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def  area(self):
        return size ** 2

    def my_print(self):
        if size == 0:
            print()
        else:
            for i in self.__size:
                print('#' * self.__size)
