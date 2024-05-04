#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes: list[list[int]]) -> bool:
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    n = len(boxes)
    # Keep track of which boxes are opened
    opened = [False] * n
    opened[0] = True  # The first box is always unlocked

    # Initialize a stack with keys from the first box
    stack = boxes[0][:]
    # Iterate through the stack until it's empty
    while stack:
        key = stack.pop()
        if key < n and not opened[key]:
            opened[key] = True
            stack.extend(boxes[key])

    # Check if all boxes are opened
    return all(opened)
