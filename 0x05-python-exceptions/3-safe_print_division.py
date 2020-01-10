#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        r = a / b
        print("Inside result: {:.1f}".format(r))
    except ZeroDivisionError:
        r = None
        print("Inside result: {}".format(r))
    finally:
        return r
