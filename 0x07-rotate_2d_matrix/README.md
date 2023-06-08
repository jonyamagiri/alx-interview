# 0x07. Rotate 2D Matrix


> This repository contains the tasks for `Rotate 2D Matrix` project and a description of what each program or function does:


## Learning Objectives

* The rotation of a 2D matrix interview question involves rotating a square matrix by 90 degrees clockwise. To rotate a matrix by 90 degrees clockwise, we can perform the following steps:
1. Transpose the matrix: Swap the elements along the main diagonal (top-left to bottom-right).
2. Reverse each row: Reverse the order of elements in each row.


## Tasks

### Task: 0-rotate_2d_matrix.py

* Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.
- [x] Prototype: `def rotate_2d_matrix(matrix):`
- [x] Do not return anything. The matrix must be edited **in-place**.
- [x] You can assume the matrix will have 2 dimensions and will not be empty.
- [x] The program should rotate given 2D matrix it 90 degrees clockwise and print it.
    * Format: see example
    ```
        ubuntu$ ./main_0.py
        [[7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]]
        ubuntu$
    ```
    * You don’t have to print the solutions in a specific order
- [x] You are only allowed to import the `sys` module



