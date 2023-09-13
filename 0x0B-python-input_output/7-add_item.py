#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file:"""

import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":

    del sys.argv[0]

    try:
        data = load("add_item.json")
        data.extend(sys.argv)
        save(data, "add_item.json")
    except FileNotFoundError:
        save(sys.argv, "add_item.json")
