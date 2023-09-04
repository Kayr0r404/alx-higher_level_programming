#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.
    Args:
    @matrix: input list of lists
    @div: input int/float to divide each element of the matrix
    Return: a new matrix whose entries are the result of dividing the
    entries of matrix by div
    """
    size = len(matrix[0])

    for i in range(len(matrix)):
        if (len(matrix[i]) != size):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    list = []
    for i in range(len(matrix)):
        new_list = []
        for j in matrix[i]:
            new_list.append(round(j / div, 2))
        list.append(new_list)
    return (list)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
