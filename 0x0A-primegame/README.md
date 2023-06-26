# 0x0A. Prime Game


> This repository contains the tasks for `Prime Game` project and a description of what each program or function does:


## Learning Objectives

* The **Prime Game** interview question is a problem that involves finding prime numbers within a given range. You are tasked to write a program or function that takes two numbers, a start and an end, as input, and returns the count of prime numbers within that range. 

* To solve the Prime Game, one can iterate through the range of numbers, check if each number is prime using a primality test (such as trial division or the Sieve of Eratosthenes), and increment a counter whenever a prime number is found. The final count is then returned as the solution to the Prime Game.

## Tasks

### Task: 0-prime_game.py

* Maria and Ben are playing a game. Given a set of consecutive integers starting from `1` up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

* They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

- [x] Prototype: `def isWinner(x, nums)`
- [x] where `x` is the number of rounds and `nums` is an array of `n`
- [x] Return: name of the player that won the most rounds
- [x] If the winner cannot be determined, return `None`
- [x] You can assume `n` and `x` will not be larger than 10000
- [x] You cannot import any packages in this task

---


