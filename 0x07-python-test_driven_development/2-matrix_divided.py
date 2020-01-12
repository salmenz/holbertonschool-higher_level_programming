#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = matrix.copy()
    l = len(new_matrix[0])
    for i in range (len(new_matrix)):
        if type(new_matrix[i]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(new_matrix[i]) != l:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(new_matrix[i])):
            if type(new_matrix[i][j]) != int and type(new_matrix[i][j]) != float:
               raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
    return new_matrix
