#!/usr/bin/python3
'''Island gal'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    counter = 0
    max_g = len(grid) - 1
    mlst = len(grid[0]) - 1

    for lst_ixd, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                if land_idx == 0:
                    counter += 1
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == mlst:
                    if lst[land_idx - 1] == 0:
                        counter += 1
                    counter += 1
                else:
                    if lst[land_idx - 1] == 0:
                        counter += 1
                    if lst[land_idx + 1] == 0:
                        counter += 1

                if lst_ixd == 0:
                    counter += 1
                    if grid[lst_ixd + 1][land_idx] == 0:
                        counter += 1
                elif lst_ixd == max_g:
                    if grid[lst_ixd - 1][land_idx] == 0:
                        counter += 1
                    counter += 1
                else:
                    if grid[lst_ixd - 1][land_idx] == 0:
                        counter += 1
                    if grid[lst_ixd + 1][land_idx] == 0:
                        counter += 1

    return counter
