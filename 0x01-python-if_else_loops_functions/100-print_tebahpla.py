#!/usr/bin/python3

for x in range(0, 26, 2):
    print("{:c}{:c}".format(122 - x, (122 - x - 1) - 32), end="")
