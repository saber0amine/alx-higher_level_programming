#!/usr/bin/python3
import json
from sys import argv
import os


if __name__ == '__main__':
    save_json_file = __import__("7-save_to_json_file").save_to_json_file
    load_json_file = __import__("8-load_from_json_file").load_from_json_file
    if not os.path.exists("add_item.json"):
        with open("add_item.json", "a") as f:
            pass
        save_json_file([], "add_item.json")
    save_json_file(load_json_file("add_item.json") + argv[1:], "add_item.json")
