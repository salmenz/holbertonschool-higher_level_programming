#!/usr/bin/python3
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
import json
import sys


filename = 'add_item.json'
try:
    File = load_from_json_file(filename)
except:
    File = []
for args in sys.argv[1:]:
    File.append(args)
save_to_json_file(File, filename)
