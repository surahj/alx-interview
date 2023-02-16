#!/usr/bin/python3
"""
Rotate 2D Matrix
"""
import copy


def rotate_2d_matrix(matrix):
    """
    Function that takes n x n 2D matrix, rotate it 90 degrees clockwise
    Args:
      matrix: n x n matrix
    Return:
      matrix that has been rotated
    """
    matrix_copy = copy.deepcopy(matrix)
    matrix_len = len(matrix)

    for i in range(matrix_len):
        for j in range(matrix_len):
            matrix[i][j] = matrix_copy[matrix_len-1-j][i]

    return matrix
