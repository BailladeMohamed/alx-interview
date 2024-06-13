#!/usr/bin/python3
""" matrix 2d"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix 90° clockwise
    returns 0"""
    left, r = 0, len(matrix) - 1

    while left < r:
        for i in range(r - left):
            t, b = left, r
            topLeft = matrix[t][left + i]
            matrix[t][left + i] = matrix[b - i][left]
            matrix[b - i][left] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = topLeft
        r -= 1
        left += 1
