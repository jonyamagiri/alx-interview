# 0x02. Minimum Operations

> This repository contains the tasks for `Minimum Operations` project and a description of what each program or function does:


## Learning Objectives

* The "Minimum Operations" technical interview question typically involves finding the minimum number of operations required to transform one input into another using a given set of operations. The specific details of the question may vary, but the general approach involves analyzing the problem, identifying possible operations, and devising an algorithm to find the minimum number of operations.


## Tasks

### Task: 0-minoperations.py

* In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n H` characters in the file.
- [x] Prototype: `def minOperations(n)`
- [x] Returns an integer
- [x] If `n` is impossible to achieve, return `0`

```
Example:
n = 9
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```


