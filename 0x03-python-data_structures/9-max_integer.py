#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return my_list
    maxu = my_list[0]
    for num in my_list:
        if num > maxu:
            maxu = num
    return maxu
