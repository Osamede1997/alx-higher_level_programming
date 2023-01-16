#!/usr/bin/python3
"""Defines a returns string to JSON function"""

import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object"""
    return json.dumps(my_obj)
