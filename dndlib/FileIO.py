#!/usr/bin/python3

import json, os.path
from pathlib import Path

"""Looks for a filename and returns either the decoded JSON object or {}

returns The opened or empty dict
"""
def get_data_from_json_file(filename, create_if_missing=True): 
    value = {}

    if create_if_missing and not Path(filename).is_file():
        try:
            with open(filename, 'w') as datafile:
                json.dump({}, datafile)
        except Exception as e:
            print("Exception while trying to create the missing API file {}. {}".format(filename, e))

    try:
        with open(filename, 'r') as datafile:
            value = json.load(datafile)
    except Exception as e:
        print("Exception while trying to read API file {}. {}".format(filename, e))

    return value

"""Saves dict to file, overwriting by default

overwrite: True if it should overwrite, False otherwise
data: data to write

returns True on success, False otherwise
"""
def save_data_to_json_file(data, filename, overwrite=True): 
    if not overwrite: 
        if os.path.isfile(filename):
            print("File {} exists and I'm not going to overwrite it.".format(filename))
            return False

    value = {}
    succ = True
    try:
        with open(filename, 'w') as datafile:
            json.dump(data, datafile)
    except Exception as e:
        print("Exception while trying to read API file {}. {}".format(filename, e))
        succ = False


    return succ
