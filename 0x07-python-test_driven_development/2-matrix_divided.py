#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    m = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    l = len(matrix[0])
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(msg)
        if len(matrix[i]) != l:
            raise TypeError("Each row of the matrix must have the same size")
        m = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError(msg)
            if div == 0:
                raise ZeroDivisionError("division by zero")
            m.append(round(matrix[i][j] / div, 2))
        new_matrix.append(m)
    return new_matrix
