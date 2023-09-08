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
    comment_1 = "matrix must be a matrix (list of lists)"
    comment_2 = " of integers/floats"
    comment_3 = "Each row of the matrix must have the same size"
    if (not isinstance(matrix, list) or len(matrix) == 0):
        raise TypeError(comment_1 + comment_2)
    else:
        for i in matrix:
            if (not isinstance(i, list) or len(i) == 0):
                raise TypeError(comment_1 + comment_2)
            elif (len(i) != len(matrix[0])):
                raise TypeError(comment_3)
            for num in i:
                if not (isinstance(num, (int, float))):
                    raise TypeError(comment_1 + comment_2)

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    li = []
    for i in range(len(matrix)):
        new_list = []
        for j in matrix[i]:
            new_list.append(round(j / div, 2))
        li.append(new_list)
    return (li)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
