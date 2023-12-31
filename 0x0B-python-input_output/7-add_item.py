#!/usr/bin/python3
"""Saves command line args to a list and save as JSON file"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add command line args to list
my_list.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(my_list, filename)
