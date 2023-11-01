#!/usr/bin/python3
for i in range(10):
    for x in range(i + 1, 10):
        endd = ", "
        if (i == 8 and x == 9):
            endd = "\n"
        print("{}{}".format(i, x), end=endd)
