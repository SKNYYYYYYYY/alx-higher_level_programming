#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []

    for row in matrix:
        squared_row = []
        for element in row:
            result = element * element
            squared_row.append(result)
        squared.append(squared_row)
    return squared
