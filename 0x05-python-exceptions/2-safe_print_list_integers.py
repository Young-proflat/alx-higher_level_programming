#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i],end=''))
    except Exception:
            continue
