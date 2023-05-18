#!/usr/bin/python3
""" module 0-validate_utf8.py """


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list of int): List of integers representing the bytes
         of the data set.
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for num in data:
        if num & 0b11000000 == 0b10000000:
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            if num_bytes != 0:
                return False

            if num & 0b10000000 == 0:
                num_bytes = 0
            elif num & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif num & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif num & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False

    return num_bytes == 0
