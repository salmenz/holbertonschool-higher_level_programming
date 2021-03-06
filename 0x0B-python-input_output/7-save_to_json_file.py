#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="UTF-8") as File:
        txt = json.dump(my_obj, File)
        return txt
