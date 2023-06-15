# 0x08. Making Change


> This repository contains the tasks for `Making Change` project and a description of what each program or function does:


## Learning Objectives

* The [Making Change problem](https://en.wikipedia.org/wiki/Change-making_problem) is a common interview question in computer science and programming. It asks you to design an algorithm to determine the minimum number of coins needed to make change for a given amount. 
* The [Greedy Algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm) is a common approach to solving this problem, and it involves repeatedly choosing the largest denomination coin that is smaller than the remaining amount, subtracting its value from the remaining amount, and incrementing the count of coins used. This process continues until the remaining amount becomes zero.

## Tasks

### Task: 0-making_change.py

* Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

- [x] Prototype: `def makeChange(coins, total)`
- [x] Return: fewest number of coins needed to meet `total`
    * If `total` is `0` or less, return `0`
    * If `total` cannot be met by any number of coins you have, return `-1`
- [x] `coins` is a list of the values of the coins in your possession
- [x] The value of a coin will always be an integer greater than `0`
- [x] You can assume you have an infinite number of each denomination of coin in the list
- [x] Your solution’s runtime will be evaluated in this task

---


