#!/usr/bin/python3
def print_last_digit(number):
    """ accept integerand print it last digit """
    print(abs(number) % 10, end='')
    return(abs(number) % 10)
