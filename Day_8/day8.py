#!/usr/bin/env python

"""
Filename: day8.py
Author: Nero
Description:
Usage:
"""

import pprint
INPUT_FILE = "Day_8/input.txt"


def get_data(file: str = INPUT_FILE) -> list:
    """Function that gets data from file

    Args:
        file (str, optional): File. Defaults to INPUT_FILE.

    Returns:
        str: data
    """
    with open(file, mode="r", encoding="utf-8") as input_file:
        data = [list(line.strip('\n')) for line in input_file]
    return data

# TODO: c'est pas is_aligned mais quelle direction et distance entre les deux
# ensuite c'est vérifier si l'antinode potentiel est situé dans le tableau
# et si ce dernier est dedans s'assurer qu'on ne le compte pas deux fois.


def get_distance_x(coord1, coord2):
    return coord1[0]-coord2[0]


def get_distance_y(coord1, coord2):
    return coord1[1]-coord2[1]


def get_antinode(data, antinodes: set, coord_1: tuple, coord_2: tuple):
    antinode_y = 0
    antinode_x = 0
    x = get_distance_x(coord_1, coord_2)
    y = get_distance_y(coord_1, coord_2)
    antinode_x = coord_1[0]+x
    antinode_y = coord_1[1]+y
    if 0 <= antinode_x <= len(data)-1 and 0 <= antinode_y <= len(data[0])-1:
        antinodes.add((antinode_x, antinode_y))
    antinode_x = coord_2[0]-x
    antinode_y = coord_2[1]-y
    if 0 <= antinode_x <= len(data)-1 and 0 <= antinode_y <= len(data[0])-1:
        antinodes.add((antinode_x, antinode_y))


def get_antinode_part_two(data, antinodes: set, coord_1, coord_2):
    antinode_y = coord_1[1]
    antinode_x = coord_1[0]
    x = get_distance_x(coord_1, coord_2)
    y = get_distance_y(coord_1, coord_2)
    while 0 <= antinode_x <= len(data)-1 and 0 <= antinode_y <= len(data[0])-1:
        antinodes.add((antinode_x, antinode_y))
        antinode_x += x
        antinode_y += y
    antinode_y = coord_2[1]
    antinode_x = coord_2[0]
    while 0 <= antinode_x <= len(data)-1 and 0 <= antinode_y <= len(data[0])-1:
        antinodes.add((antinode_x, antinode_y))
        antinode_x -= x
        antinode_y -= y


def check_antinodes_part_2(data, antennas):
    antinodes = set()
    for elt in antennas:
        for i in range(0, len(antennas[elt])):
            for j in range(0, len(antennas[elt])):
                if j == i:
                    continue
                get_antinode_part_two(data, antinodes, list(antennas[elt])[
                    i], list(antennas[elt])[j])
    print(len(antinodes))


def check_antinodes(data, antennas):
    antinodes = set()
    for elt in antennas:
        for i in range(0, len(antennas[elt])):
            for j in range(0, len(antennas[elt])):
                if j == i:
                    continue
                get_antinode(data, antinodes, list(antennas[elt])[
                             i], list(antennas[elt])[j])
    print(len(antinodes))


if __name__ == "__main__":
    from collections import defaultdict
    import string
    data_list = get_data()
    data_check = data_list.copy()
    antennas = defaultdict(set)
    for i in range(0, len(data_check)):
        for j in range(0, len(data_check[0])):
            if data_check[i][j] in string.ascii_letters+string.digits:
                line = i
                row = j
                if data_check[i][j] == 'f':
                    pass
                antennas[data_check[i][j]].add((line, row))
    pprint.pprint(antennas)
    check_antinodes(data_list, antennas)
    check_antinodes_part_2(data_list, antennas)
