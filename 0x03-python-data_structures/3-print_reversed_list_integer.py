#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new = my_list.copy()
    for i in reversed(new):
        print(i)
