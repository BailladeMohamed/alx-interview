#!/usr/bin/python3

"""Module for unlocking boxes"""


def canUnlockAll(boxes):
    """
    Function to verify if every single box can be unlocked.
    boxes : list of lists where each sublist
    represents a box and contains keys.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [key for key in boxes[0] if key < n]

    while keys:
        new_keys = []
        for key in keys:
            if not unlocked[key]:
                unlocked[key] = True
                for k in boxes[key]:
                    if k < n and not unlocked[k]:
                        new_keys.append(k)
        keys = new_keys

    return all(unlocked)
