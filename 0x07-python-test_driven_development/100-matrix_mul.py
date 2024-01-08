#!/usr/bin/python3
"""Model that produces a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrixes if thei're rectangular
        and returns a new matrix.
    Args:
        m_a(list of lists of integers or floats): firs matrix
        m_b(list of lists of integers or floats): second matrix
    Returns: a new matrix(result)
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        for value in row:
            if not isinstance(value, int) and not isinstance(vaule, float):
                raise ValueError("m_a should contain only integers or floats")
        m_a_row_lenght = len(m_a[0])
        if len(row) != m_a_row_lenght:
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        for value in row:
            if type(value) is not int and type(value) is not float:
                raise ValueError("m_b should contain only integers or floats")
        m_b_row_lenght = len(m_b[0])
        if len(row) != m_b_row_lenght:
            raise TypeError("each row of m_b must be of the same size")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_b)):
                value += m_a[i][k] * m_b[k][j]
            result_row.append(value)
        result.append(result_row)
    return result
