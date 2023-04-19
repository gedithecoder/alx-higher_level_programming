#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = [[j * j for j in row] for row in matrix]
    return new
