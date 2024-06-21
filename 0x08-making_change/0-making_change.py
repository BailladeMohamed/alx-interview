#!/usr/bin/python3
""" from within come change """


def makeChange(coins, total):
    """takes a list of coins and use
       it to cal the total
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        gege = 0
        for gojo in coin:
            while(total >= gojo):
                gege += 1
                total -= gojo
        if total == 0:
            return gege
        return -1
