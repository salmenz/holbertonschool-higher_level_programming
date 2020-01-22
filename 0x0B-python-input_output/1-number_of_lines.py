#!/usr/bin/python3
def number_of_lines(filename=""):
    len = 0
    with open(filename, encoding="UTF-8") as File:
        while True:
            line = File.readline()
            if not line:
                break
            len += 1
    return len
