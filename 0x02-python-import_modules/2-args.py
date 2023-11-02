#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = "arguments:"
    argc = len(sys.argv) - 1
    if (argc == 0):
        arg = "arguments."
    if (argc == 1):
        arg = "argument:"
    print("{} {}".format(argc, arg))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
