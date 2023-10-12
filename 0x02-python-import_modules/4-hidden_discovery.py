#!/usr/bin/python3

import dis
import importlib

def print_names(module_name):
    try:
        module = importlib.import_module(module_name)
        names = [name for name in dir(module) if not name.startswith("__")]
        names.sort()
        for name in names:
            print(name)
    except Exception as e:
        pass

if __name__ == "__main__":
    module_name = "hidden_4"
    print_names(module_name)
