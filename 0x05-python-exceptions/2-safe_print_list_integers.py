#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    for i in range(x):
        len += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
    print()
    return len
