# 0x09. Island Perimeter


> This repository contains the tasks for `Island Perimeter` project and a description of what each program or function does:


## Learning Objectives

* The **Island Perimeter** problem is a common tech interview question that involves calculating the perimeter of an island represented by a grid. The grid consists of 0's and 1's, where 0 represents water and 1 represents land. The goal is to find the perimeter of the island, assuming that the cells are connected horizontally and vertically.

* To solve the Island Perimeter problem, we can follow this approach: Initialize a variable called perimeter to 0. Traverse the grid and for each land cell, increase the perimeter by 4. Then, check the neighboring cells and decrease the perimeter by 1 for each neighboring land cell. Finally, the perimeter variable will hold the total perimeter of the island.

## Tasks

### Task: 0-island_perimeter.py

* Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- [x] `grid` is a list of list of integers:
    * 0 represents water
    * 1 represents land
    * Each cell is square, with a side length of 1
    * Cells are connected horizontally/vertically (not diagonally).
- [x] `grid` is rectangular, with its width and height not exceeding 100
- [x] The grid is completely surrounded by water
- [x] There is only one island (or nothing).
- [x] The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

---


