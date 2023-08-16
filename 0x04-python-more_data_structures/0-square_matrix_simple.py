#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in range(len(matrix)):
        list = []
        for j in range(len(matrix[i])):
            list.append(matrix[i][j] ** 2)
        newMatrix.append(list)
    return (newMatrix)
