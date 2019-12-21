#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) is not str:
        return(0)
    else:
        sum = 0
        tuple1 = ("I", "V", "X", "L", "C", "D", "M")
        tuple2 = (1, 5, 10, 50, 100, 500, 1000)
        for i in range(len(roman_string)):
            for j in range(len(tuple1)):
                if roman_string[i] == tuple1[j]:
                    if tuple2[j] <= tuple2[j+1] and tuple2[j+1] != None:
                        sum += tuple2[j]
                    else:
                        sum -= tuple2[j]
    return(sum)
