#!/usr/bin/python3

# check if name == main to prevent err
if __name__ == "__main__":
    import sys

num_args = len(sys.argv) - 1
if num_args == 0:
    print("0 argument")
elif num_args == 1:
    print("1 arguments:")
else:
    print("{} arguments:".format(num_args))
