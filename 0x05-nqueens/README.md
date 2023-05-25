# 0x05. N Queens

> This repository contains the tasks for `N Queens` project and a description of what each program or function does:


## Learning Objectives

* The **N Queens** problem is a classic computer science problem that asks to find all possible ways to place N non-attacking queens on an N×N chessboard. The problem is known to be NP-hard, meaning that it is very difficult to solve for large values of N. However, there are a number of algorithms that can be used to find solutions to the problem.

* One common approach to solving the N Queens problem is to use a [backtracking](https://en.wikipedia.org/wiki/Backtracking) algorithm. A backtracking algorithm works by trying all possible combinations of queen placements until it finds a solution. If the algorithm finds a solution, it returns the solution. Otherwise, the algorithm backtracks and tries a different combination of queen placements.


## Tasks

### Task: 0-nqueens.py

* Write a program that solves the N queens problem.
- [x] Usage: `nqueens N`
    * If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- [x] where N must be an integer greater or equal to `4`
    * If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
    * If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- [x] The program should print every possible solution to the problem
    * One solution per line
    * Format: see example
    ```
        ubuntu@ubuntu:~$ ./0-nqueens.py 4
        [[0, 1], [1, 3], [2, 0], [3, 2]]
        [[0, 2], [1, 0], [2, 3], [3, 1]]
        ubuntu@ubuntu:~$ ./0-nqueens.py 6
        [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
        [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
        [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
        [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
    ```
    * You don’t have to print the solutions in a specific order
- [x] You are only allowed to import the `sys` module
