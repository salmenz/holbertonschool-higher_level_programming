#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    m = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    l = len(matrix[0])
    if len(matrix) == 0:
        raise TypeError(msg)
    for i in range(len(matrix)):
        if (len(matrix))[i] == 0:
            raise TypeError(msg)
        if type(matrix[i]) != list:
            raise TypeError(msg)
        if len(matrix[i]) != l:
            raise TypeError("Each row of the matrix must have the same size")
        m = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError(msg)
            if type(div) is not float and type(div) is not int:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
             if div == float('inf') or div == -float('inf') or div != div:
                m.append(round(0 / 1, 2))
            else:
                m.append(round(matrix[i][j] / div, 2))
        new_matrix.append(m)
    return new_matrix
