#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """squares elemenst of a matrix
    Args:
        matrix(list of lists):the target matrix
    """
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (new_matrix)
