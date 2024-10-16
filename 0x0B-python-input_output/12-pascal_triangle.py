#!/usr/bin/python3
"""
This module defines the function pascal_triangle
"""


def pascal_triangle(n):
    """Function to generate a triangle"""
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
