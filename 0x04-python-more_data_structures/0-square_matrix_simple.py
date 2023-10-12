#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        row = matrix[i]
        squared_row = []

        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)
            result.append(squared_row)

    return (result)
