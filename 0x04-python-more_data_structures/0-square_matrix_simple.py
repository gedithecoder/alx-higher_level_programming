#!/usr/bin/python3

def square_matrix_simple(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = matrix[i][j] * matrix[i][j]
