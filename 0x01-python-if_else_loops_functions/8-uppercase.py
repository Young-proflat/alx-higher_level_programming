#!/usr/bin/python3
""" accept string and convert in to a capital letter """
def uppercase(str):
    """ accept an argument and saves it in result """
    result = " "
    """ iterate through the argument """
    for i in str:
        if ord(i) >= 65:
            result += chr(ord(i) - 32)
    return result

