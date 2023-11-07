#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for i in range(0, len(matrix)):
            for x in range(0, len(matrix[i])):
                separator = " "
                if (x == len(matrix[i]) - 1):
                    separator = ""
                print("{}{}".format(matrix[i][x], separator), end="")
            print("")
