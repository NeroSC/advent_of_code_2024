#!/usr/bin/env python

"""
Filename: day6.py
Author: Nero
Description:
Usage:
"""

import pprint
INPUT_FILE = "Day_6/input.txt"


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


def get_guard_position(data):
    up = 1
    right = 2
    left = 3
    down = 4
    position = 0
    for i, _ in enumerate(data):
        for char in data[i]:
            if char != "#" and char != '.':
                if char == "^":
                    position = up
                elif char == ">":
                    position = right
                elif char == "v":
                    position = down
                elif char == "<":
                    position = left
                return i, data[i].index(char), position


def move(data):
    unique_positions = set()
    data_test=copy.deepcopy(data)
    line, col, orientation = get_guard_position(data_test)
    ligne, column, orient = get_guard_position(data_test)
    line,col,orientation=ligne,column,orient
    loop = 0
    while 0 <= line <= len(data_test) and 0 <= col <= len(data_test[0]):
        if loop > 1000:
            # todo make faster
            return (loop)
        loop += 1
        if orientation == 1:
            while data_test[line-1][col] != "#":
                unique_positions.add((line, col))
                data_test[line][col] = '.'
                line -= 1
                data_test[line][col] = '^'
                if line-1 < 0:
                    unique_positions.add((line, col))
                    data_test[line][col]='.'
                    data_test[ligne][column]='^'
                    return (unique_positions)
                # pprint.pprint(data)
            data_test[line][col] = '>'
            orientation = 2
        elif orientation == 2:
            while data_test[line][col+1] != "#":
                unique_positions.add((line, col))
                data_test[line][col] = '.'
                col += 1
                if col+1 > len(data_test[0])-1:
                    unique_positions.add((line, col))
                    data_test[ligne][column]='^'
                    data_test[line][col]='.'
                    return (unique_positions)
                data_test[line][col] = '>'
                # pprint.pprint(data)
            data_test[line][col] = 'v'
            orientation = 3
        elif orientation == 3:
            while data_test[line+1][col] != "#":
                unique_positions.add((line, col))
                data_test[line][col] = '.'
                line += 1
                if line+1 > len(data_test)-1:
                    unique_positions.add((line, col))
                    data_test[ligne][column]='^'
                    data_test[line][col]='.'
                    return (unique_positions)
                data_test[line][col] = 'v'
                # pprint.pprint(data)
            data_test[line][col] = '<'
            orientation = 4
        else:
            while data_test[line][col-1] != "#":
                unique_positions.add((line, col))
                data_test[line][col] = '.'
                col -= 1
                if col-1 < 0:
                    unique_positions.add((line, col))
                    data_test[ligne][column]='^'
                    data_test[line][col]='.'
                    return (unique_positions)
                data_test[line][col] = '<'
                # pprint.pprint(data)
            data_test[line][col] = '^'
            orientation = 1


def test_loop(data, unique_position,line,col):
    block=0
    for i, j in unique_position:
        if (line,col)!=(i,j):
            data[i][j] = "#"
            loop=move(data)
            data[i][j] = "."
            if loop==1001:
                block+=1
    return block


if __name__ == "__main__":
    import copy
    data_list = get_data()
    data_list_2 = copy.deepcopy(data_list)
    line, col, orientation = get_guard_position(data_list)
    unique_pos = move(data_list)
    print(test_loop(data_list_2, unique_pos,line,col))
