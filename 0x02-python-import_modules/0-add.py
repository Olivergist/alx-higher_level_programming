#!/usr/bin/python3

# we import the module
from add_0 import add

def main():
    # Assign thr values to store in a and b
    a = 1
    b = 2

    # We calculate the result using the imported function
    result = add(a, b)

    # Display the result
    print("{} + {} = {}".format(a, b, result))

    if __name__ == "__main__":
        # Call the main function only when the script is run directly
        main()
