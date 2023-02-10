#!/usr/bin/python3
"""
method that calculates the fewest no of opperations to get the result in exactly n H chara in a file
"""
def minOperations(n):
    """ min operations method"""
    
    if n <= 1:
        return 0
    operations = 0
    for i in range(2, n+1):
        while n % i == 0:
            operations += i
            n = n // i
    return operations