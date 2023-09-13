#!/usr/bin/python3
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

del sys.argv[0]

try:
    data = load("add_item.json")
    data.extend(sys.argv)
    save(data, "add_item.json")
except FileNotFoundError:
    save(sys.argv, "add_item.json")
