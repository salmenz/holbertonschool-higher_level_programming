#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="UTF-8") as File:
        print ("{:s}".format(File.read()), end="")
