#!/usr/bin/env python3
def no_c(my_string):
    str = ""
    i = 0
    while i < len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            str = str + my_string[i]
        i += 1
    return(str)
