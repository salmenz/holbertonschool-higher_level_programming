#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a", encoding="UTF8") as File:
        return File.write(text)
