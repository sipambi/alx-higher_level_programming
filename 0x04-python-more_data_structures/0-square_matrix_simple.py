#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = matrix.copy()

    for i in matrix:
        newMatrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (newMatrix)
