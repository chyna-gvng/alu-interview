#!/usr/bin/python3
"""
    0-rain
"""

def rain(walls):
    """
    Parameters:
        walls: ist of non-negative integers

    Returns:
        int: total amount of rainwater collected
    """
    if walls is None:
        return 0

    walls_length = len(walls)
    max_water = 0

    if walls == 0 or walls_length == 1:
        return 0

    for i in range(1, walls_length - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, walls_length):
            right = max(right, walls[j])
        max_water = max_water + (min(left, right) - walls[i])
    return max_water