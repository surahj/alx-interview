#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    A function that returns the perimeter of the island described in grid
    Args:
        grids: a list of list of integers

    Returns:
        the perimeter of the island described in grid
    """
    counter = 0
    for i, value in enumerate(grid):
        for j in range(len(value)):
            if value[j] == 1 and i != 0 and i != len(grid) - 1:
                if grid[i-1][j] == 0:
                    counter += 1

                if grid[i][j-1] == 0:
                    counter += 1

                if grid[i][j+1] == 0:
                    counter += 1

                if grid[i+1][j] == 0:
                    counter += 1
    return counter
