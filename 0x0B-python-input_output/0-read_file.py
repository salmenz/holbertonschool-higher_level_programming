#!/usr/bin/python3
def read_file(filename=""):
    """ Function that read a text file (UTF8) and prints it stdout """
    with open(filename, encoding="UTF-8") as File:
        print ("{:s}".format(File.read()), end="")
