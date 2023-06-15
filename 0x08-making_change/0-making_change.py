#!/usr/bin/python3
""" module 0-making_change """


def makeChange(coins, total):
    """
    Calculates the least number of coins needed to make change
     for a given total.
    """
    if total < 1:
        return 0

    # Sort coins in descending order; ensures the largest coins are used first
    coins.sort(reverse=True)
    least = 0

    # Iterate over the coins; if total <= 0, exit loop
    for coin in coins:
        if total <= 0:
            break

        # find number of coins needed to make change for the current coin
        # Increment the number of coins needed for the current coin
        # Subtract the number of coins needed for the current
        count = total // coin
        least += count
        total -= count * coin

    return -1 if total != 0 else least
