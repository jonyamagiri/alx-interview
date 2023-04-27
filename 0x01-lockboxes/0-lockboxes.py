#!/usr/bin/python3
""" module 0-lockboxes.py """


def canUnlockAll(boxes):
    """
    Determines whether all the boxes in a list of locked boxes can be opened.
    Args:
        boxes (list): A list of n lists, where each list represents a locked
         box and contains the keys to other boxes. Each box is numbered
          sequentially from 0 to n - 1.
    Returns:
        bool: True if all boxes can be opened, else if False.
    """
    n = len(boxes)
    # Initialize a list of booleans indicating whether each box has been
    # unlocked yet
    unlocked = [False] * n
    unlocked[0] = True  # The first box is already unlocked
    stack = [0]  # Initialize a stack with the first box to explore

    while stack:
        box = stack.pop()  # Pop the next box to explore from the stack
        for key in boxes[box]:  # Try to unlock all the boxes that this
            # box has keys for
            # Only try to unlock boxes that are within the range of the box
            # list and haven't already been unlocked
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)  # True if all boxes have been unlocked, else False
