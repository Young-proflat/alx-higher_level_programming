#!/usr/bin/python3
""" accept string and convert in to a capital letter """
def uppercase(str):
    """ accept an argument and saves it in result """
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print('{}'.format(i), end='')
    print()

