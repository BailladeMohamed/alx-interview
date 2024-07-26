#!/usr/bin/python3
"""
Thee pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n <= 0:
        return []

    pascal = [[1]]
    for G in range(1, n):
        row = [1]
        L_R = pascal[-1]
        for index in range(1, G):
            row.append(L_R[index-1] + L_R[index])
        row.append(1)
        pascal.append(row)
    return pascal
