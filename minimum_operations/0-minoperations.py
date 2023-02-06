#!/usr/bin/python3
"""
method that calculates the fewest no of opperations to get the result in exactly n H chara in a file
"""


def minOperations(n):
    """
    min operations method
    """
    if n <= 1:
        return 0
    operations = 0
    A = 1
    copyall = 0
    paste = 0
    A_copied = 0
    while A < n:
        if n % A == 0:
            copyall += 1
            A_copied = A
        paste += 1
        operations = copyall + paste
        A += A_copied
    return operations
