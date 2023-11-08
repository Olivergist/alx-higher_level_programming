#!/usr/bin/python3
"""Inserts line after lines containing specific string in file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after lines containing search_string"""
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
        f.seek(0)
        f.writelines(lines)
