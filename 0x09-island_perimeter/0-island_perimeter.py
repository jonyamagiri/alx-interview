#!/usr/bin/python3
""" module 0-island_perimeter """


def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid.
    Args:
        grid (list): A 2D grid representing the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check neighbors to subtract shared edges
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i+1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if j < cols - 1 and grid[i][j+1] == 1:
                    perimeter -= 1

    return perimeter
