#!/usr/bin/python3
""" Module 0-prime_game """


def is_prime(n):
    """Checks whether a number is prime.
    Args:
        n (int): The number to be checked.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(n, primes):
    """ Generates prime numbers up to n and store them in the primes list """
    last_prime = primes[-1]
    primes.extend([i for i in range(last_prime + 1, n + 1) if is_prime(i)])


def isWinner(x, nums):
    """Determines the winner of the prime game; returns name of the winner,
     or none if its a tie.
    Args:
        x (int): The number of rounds.
        nums (List[int]): A list of integers representing the rounds.
    """
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]  # list of initial prime numbers
    generate_primes(max(nums), primes)  # generate primes upto number in 'nums'

    for round in range(x):
        prime_count = sum((i != 0 and i <= nums[round])
                          for i in primes[:nums[round] + 1])
        # determine winner of the current round based on prime count
        winner = "Maria" if prime_count % 2 else "Ben"
        score[winner] += 1

    # compare number of wins; return winner or None if they tie
    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
