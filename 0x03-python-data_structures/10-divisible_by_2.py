#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        if not i % 2:
            new.append(True)
        else:
            new.append(False)
    return new
