#!/usr/bin/python3

# Check if this script is run
if __name__ == "__main__":
    # Import the hidden_4 module
    import hidden_4

    # Get a list of all names defined
    names = dir(hidden_4)

# Iterate through each name in the list
for name in names:
# Check if the name does not start
    if name[:2] != "__":
    # Print the public names
print(name)
