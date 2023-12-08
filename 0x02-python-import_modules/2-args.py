#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys

j = len(sys.argv)
no_args = j
if no_args == 2:
    print("{} argument:".format(no_args - 1))
elif no_args == 1:
    print("0 arguments.")

else:
    print("{} arguments:".format(no_args - 1))

i = 1
while i < no_args:
    print("{} : {}".format(i, sys.argv[i]))
    i += 1
