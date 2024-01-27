#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    nb = sorted(a_dictionary.keys())

    for k in nb:
        print("{:s}: {}".format(k, a_dictionary[k]))
