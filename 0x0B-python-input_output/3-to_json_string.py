#!/usr/bin/python3
"""Function to return JSON"""

import json


def to_json_string(my_obj):
    """Return JSON representation of an object"""
    return json.dumps(my_obj)
