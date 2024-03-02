#!/usr/bin/python3
""" add two integer together"""


def add_integer(a, b=98):
    """A function that return int(a) + int(b)."""
    if type(a) is not an int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not an int and type(b) is not float:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
