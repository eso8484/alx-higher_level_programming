#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys

j = len(sys.argv)
no_args = j - 1
if no_args == 0:
    print("{} arguments.".format(no_args))
elif no_args == 1:
    print("1 argument:")

else:
    print("{} arguments:".format(no_args))

i = 1
while i <= no_args:
    print("{}: {}".format(i, sys.argv[i]))
    i += 1
