#!/usr/bin/python3


def matrix_divided(matrix, div):
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")


    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    first_row_len = len(matrix[0])
    for row in matrix:
        if first_row_len != len(row):
             raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for  i in row:
                if (type(i) not in [int, float]):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    quotte = round(i/div, 2)
                    new_row.append(quotte)
        new_matrix.append(new_row)

    return new_matrix
