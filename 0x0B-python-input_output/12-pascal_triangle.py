#!/usr/bin/python3
def pascal_triangle(n):
    list = []
    if n <= 0:
        return list
    else:
        for i in range(1, n):
            inner_list = [1]
            if len(inner_list) < i:
                for j in range(i):
                    inner_list.append(i)
                inner_list.append(1)
            list.append(inner_list)
    return list
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))