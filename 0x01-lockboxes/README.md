# 0x01-lockboxes

# 0x01. Lockboxes

> This repository contains the tasks for `Lockboxes` project and a description of what each program or function does:


## Learning Objectives

* The lockboxes question is a common technical interview question that tests a candidate's ability to solve problems with data structures and algorithms. In this question, you are given a list of n locked boxes, each numbered from 0 to n-1. Each box contains a list of keys that can be used to open other boxes. You are required to write a function `canUnlockAll` that returns a boolean value indicating whether it is possible to open all the boxes starting from the first box. The first box is already unlocked.

* To solve this problem, you need to find a way to keep track of the boxes that have been unlocked and the boxes that still need to be explored. One possible solution is to use a stack to keep track of the boxes that need to be explored. You can start by exploring the first box and adding all the keys to the stack. Then, while the stack is not empty, you can pop a box from the stack, unlock it, and add all its keys to the stack. You can also keep track of the boxes that have been unlocked using a list of booleans. If all boxes are unlocked at the end of this process, you can return `True`, otherwise you can return `False`.


## Tasks

### Task: 0-lockboxes.py

* You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
- [x] Prototype: `def canUnlockAll(boxes)`
- [x] `boxes` is a list of lists
- [x] A key with the same number as a box opens that box
- [x] You can assume all keys will be positive integers
    - There can be keys that do not have boxes
- [x] The first box `boxes[0]` is unlocked
- [x] Return `True` if all boxes can be opened, else return False



