#!/usr/bin/python3
def safe_print_division(a,b):
    rst = 0
    try:
        rst = (a/b)
    except Exception:
        rst = None
    finally:
        Print('Inside result: {}'.format(rst))
    return rst
