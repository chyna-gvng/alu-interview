#!/usr/bin/python3
"""
    0-rain
"""

def rain(walls):
  """
  Calculates the amount of water retained after it rains.

  Args:
    walls: A list of non-negative integers representing the heights of walls with unit width 1.

  Returns:
    The amount of water retained, in square units.
  """

  # Initialize the amount of water retained to 0.
  water_retained = 0

  # Iterate through the walls, from left to right.
  for i in range(len(walls)):

    # If the current wall is higher than the previous wall, then there is water that can be retained.
    if walls[i] > walls[i - 1]:

      # Find the index of the first wall that is lower than the current wall.
      index = i
      while index < len(walls) or walls[index] >= walls[i]:
        index += 1

      # Check if the index is less than the length of the list.
      if index < len(walls):
        # Calculate the amount of water that can be retained.
        water_retained += (index - i) * walls[i]

  # Return the amount of water retained.
  return water_retained
