#!/usr/bin/python3


def canUnlockAll(boxes):
    """Determine if all boxes can be opened."""
    # Check if boxes is a list and if it's not empty
    if type(boxes) is not list or len(boxes) == 0:
        return False

    n = len(boxes)
    keys = [0]
    opened = [False] * n
    opened[0] = True

    while keys:
        key = keys.pop()
        for box in boxes[key]:
            if box < n and not opened[box]:
                keys.append(box)
                opened[box] = True

    # Check if all boxes can be opened
    for G in range(1, n):
        if not opened[G]:
            return False

    return True
