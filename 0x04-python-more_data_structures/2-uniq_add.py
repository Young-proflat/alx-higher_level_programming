#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = 0
    uniq_nom = set(my_list)

    for no in uniq_nom:
        unique_num += no
    return (unique_num)
