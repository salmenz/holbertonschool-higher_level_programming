#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "a", encoding="UTF8") as File:
        return File.write(text)
