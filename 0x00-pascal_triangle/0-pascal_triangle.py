#!/usr/bin/python3
"""
pascal triangle that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    if (n <= 0):
        return []

    pascal = []
    for i in range(n):
        pascal.append([])
        pascal[i].append(1)

        for j in range(1, i):
            pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])

        if (i != 0):
            pascal[i].append(1)

    return pascal
