#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    number_of_lines = __import__('1-number_of_lines').number_of_lines
    if number_of_lines(filename) <= nb_lines or nb_lines <= 0:
        with open(filename, encoding="UTF-8") as File:
            print(File.read())
    else:
        line = 1
        with open(filename, encoding="UTF-8") as File:
            while nb_lines >= line:
                print(File.readline())
                line += 1
            
