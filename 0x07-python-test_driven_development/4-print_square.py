#!/usr/bin/python3
""" A function that print a square with a character #"""


def print_square(size):
    """A function that prints the square of a size"""
    if type(size) is not int:
        raise TypeError('size must be an int')
    if size <= 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#') end='')
        print()

