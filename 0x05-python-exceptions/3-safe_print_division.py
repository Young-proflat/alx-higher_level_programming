#!/usr/bin/python3
def safe_print_division(a,b):
    result = 0
    try:
        t
        result = a/b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        Print('Inside result: {}'.format(result))
        return result
