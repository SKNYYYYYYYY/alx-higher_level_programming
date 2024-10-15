#!/usr/bin/python3
"""
    This module is a script that adds the command line arguments to a list
    and saves them to a JSON file.
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# check if it exists
if os.path.exists('add_item.json'):
    object = load_from_json_file('add_item.json')
else:
    object = []
object.extend(sys.argv[1:])
save_to_json_file(object, 'add_item.json')