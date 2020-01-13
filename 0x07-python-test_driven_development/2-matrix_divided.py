#!/usr/bin/python3
"""
Module matrix_divided(matrix, div)
have a function that
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of
        integers/floats")
        return

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of
            integers/floats")
            return

    for i in matrix:
        for j in i:
             if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of
                integers/floats")
                return

    l = len(matrix[0])
    for i in matrix:
        if len(i) is not l:
            raise TypeError("Each row of the matrix must have the same size")
            return

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
        return

    if div == 0:
        raise ZeroDivisionError("division by zero")
        return

    new_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            new_row.append(round((j / div), 2))
        new_matrix.append(new_row)
    return new_matrix
