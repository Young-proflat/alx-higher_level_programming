#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each symbol"""

def text_indentation(text):
    """after symbol enter a two new line"""
    symbol = [',', '.', '?']
    result = " "
    if type(text) != str:
        raise TypeError('text must be a string')
    for i in text:
        result += i
        if i in symbol:
            result += '\n\n'
            print(result)
