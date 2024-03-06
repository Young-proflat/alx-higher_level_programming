#!/usr/bin/python3
"""function that writes a string to a textfile(UTF8)and returns number"""


def write_file(filename="", text=""):
    """write a string to a text file (UTF8)"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
