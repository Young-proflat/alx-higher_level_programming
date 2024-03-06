#!/usr/bin/python3
"""Function that appends a string a the end of a text file(UTF8)"""


def append_write(filename="", text=""):
    """append a string to an existing string"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
