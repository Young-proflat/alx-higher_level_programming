#!/usr/bin/python3
"""writes an object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """write object to a textfile"""
    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))
