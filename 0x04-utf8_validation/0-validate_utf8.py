#!/usr/bin/python3
"""
validation task :)
"""


def validUTF8(data):
    """
    data: int list
    Return: is True if data is valid UTF-8
    encoding, if no return False
    """
    c_bite = 0

    for id in data:
        if c_bite == 0:
            if id >> 5 == 0b110 or id >> 5 == 0b1110:
                c_bite = 1
            elif id >> 4 == 0b1110:
                c_bite = 2
            elif id >> 3 == 0b11110:
                c_bite = 3
            elif id >> 7 == 0b1:
                return False
        else:
            if id >> 6 != 0b10:
                return False
            c_bite -= 1
    return c_bite == 0
