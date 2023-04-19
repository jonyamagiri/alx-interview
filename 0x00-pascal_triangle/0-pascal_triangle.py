#!/usr/bin/python3
""" 0-pascal_triangle.py """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Args:
        n (int): The number of rows to generate in Pascal's triangle.
    Returns:
        A list of lists of integers representing Pascal's triangle of n.
    """

    if n <= 0:
        return []  # Return empty list for n <= 0

    # Initialize Pascal's triangle with first row as [1]
    triangle = [[1]]

    # Generate Pascal's triangle using for loops
    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row from the triangle
        new_row = [1]  # Initialize new row with 1 at the beginning
        for j in range(1, i):
            # Calculate the value in the new row using the values from the
            # previous row
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Add 1 at the end of the new row
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle
