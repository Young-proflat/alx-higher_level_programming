#!/usr/bin/python3
"""creating a base class"""

import json
import csv
import os


class Base:
    """Defining a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing a class base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else: 
            self.id = id
