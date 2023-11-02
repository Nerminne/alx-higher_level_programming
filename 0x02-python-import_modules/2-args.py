#!/usr/bin/python3
import sys
if __name__ == "__main__":
    none = ":"
    argc = len(sys.argv) - 1
    if (argc == 0):
        none = "."
    print("{} arguments{}".format(argc, none))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
