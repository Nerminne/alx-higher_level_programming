#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in range(len(matrix)):
        new_matrix.append([])
        for y in range(len(matrix[x])):
            new_matrix[x].append(matrix[x][y] ** 2)
    return (new_matrix)
