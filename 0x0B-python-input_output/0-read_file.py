#!/usr/bin/python3
"""A function that reas a text file (UTF8)"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and print out an output"""
    with open(filename, encoding ="utf-8") as f:
        print(f.read(), end="")
