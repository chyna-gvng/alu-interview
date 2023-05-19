#!/usr/bin/python3
"""
    Method that calculates the fewest number of operations needed,
    to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
        Calculates the fewest number of operations needed,
        to result in exactly n H characters in the file.

        Args:
            n: The number of H characters to reach.
        Returns:
            The fewest number of operations needed.
        Raises:
            ValueError: If n is impossible to achieve.
    """

    if n <= 0:
        raise ValueError("n must be positive")

    # Initialize the DP table.
    dp = [float("inf")] * (n + 1)

    # Fill in the DP table.
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1, dp[i // 3] + 1)

    return dp[n]
