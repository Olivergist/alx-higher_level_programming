#!/usr/bin/python3
"""Function to Represented by a JSON string to an object"""
import json


def from_json_string(my_str):
    """Represented by a JSON string to an object"""
    return json.loads(my_str)
