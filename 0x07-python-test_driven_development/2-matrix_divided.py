#!/usr/bin/python3

"""Fuinctions taht divides all elements"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    param matrix: A list of lists containing integers or floats.
    param div: The number (integer or float) by which to divide all elements.
    return: A new matrix with elements divided by div,
    rounded to 2 decimal places.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a list of lists of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
