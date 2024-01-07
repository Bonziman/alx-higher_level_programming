#!/usr/bin/python3
"""This is a model for the function that devides the values of a matrix"""

def matrix_divided(matrix, div):
    """ A function to divide all the elements of a matrix
    Args:
        matrix(list of lists of integers or floats): the matrix
        div(int or float): the divisor to use
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_lenght = len(matrix[0])
    for row in matrix:
        if len(row) != row_lenght:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        divided_row = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            divided_row.append(round(value / div, 2))
        divided.append(divided_row)
    return divided
