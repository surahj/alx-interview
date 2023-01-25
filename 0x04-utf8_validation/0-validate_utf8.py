#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    remaining_bytes = 0
    for b in data:
        if remaining_bytes == 0:
            if (b & 0b10000000) == 0b00000000:
                """
                single-byte character (ASCII)
                """
                continue
            elif (b & 0b11100000) == 0b11000000:
                """
                first byte of a 2-byte character
                """
                remaining_bytes = 1
            elif (b & 0b11110000) == 0b11100000:
                """
                first byte of a 3-byte character
                """
                remaining_bytes = 2
            elif (b & 0b11111000) == 0b11110000:
                """
                first byte of a 4-byte character
                """
                remaining_bytes = 3
            else:
                return False
        else:
            if (b & 0b11000000) == 0b10000000:
                """
                continuation byte
                """
                remaining_bytes -= 1
            else:
                return False
    return remaining_bytes == 0
