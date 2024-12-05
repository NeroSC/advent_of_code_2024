#!/usr/bin/env python

"""
Filename: day3.py
Author: Nero
Description:
Usage:
"""

INPUT_FILE = "Day_4/input.txt"


def get_data(file: str = INPUT_FILE) -> list:
    """Function that gets data from file

    Args:
        file (str, optional): File. Defaults to INPUT_FILE.

    Returns:
        str: data
    """
    with open(file, mode="r", encoding="utf-8") as input_file:
        data = [line.strip('\n') for line in input_file]
    return data


def check_line(line: str):
    """Calculates de xmas in a line

    Args:
        line (str): line to check

    Returns:
        int: amount of xmas found
    """
    counter = 0
    counter += line.count("XMAS")+line.count("SAMX")
    return counter


def check_data(data: list, data_index: int, line_index: int, pattern: str):
    """Checks the rest of data diagonally

    Args:
        data (list): data list
        data_index (int): index of current data line
        line_index (int): index inside the line
        pattern (str): pattern to match

    Returns:
        int: amout of xmas found
    """
    counter = 0
    down = ""
    up = ""
    diag_up_left = ""
    diag_up_right = ""
    diag_down_left = ""
    diag_down_right = ""
    for i in range(1, 4):
        if data_index <= len(data)-4:
            down += data[data_index+i][line_index]
            if line_index >= 3:
                diag_down_left += data[data_index+i][line_index-i]
            if line_index < len(data[0])-3:
                diag_down_right += data[data_index+i][line_index+i]
        if data_index >= 3:
            up += data[data_index-i][line_index]
            if line_index >= 3:
                diag_up_left += data[data_index-i][line_index-i]
            if line_index < len(data[0])-3:
                diag_up_right += data[data_index-i][line_index+i]
    if down == pattern:
        counter += 1
    if up == pattern:
        counter += 1
    if diag_up_left == pattern:
        counter += 1
    if diag_up_right == pattern:
        counter += 1
    if diag_down_left == pattern:
        counter += 1
    if diag_down_right == pattern:
        counter += 1
    return counter


def check_around(data: list, data_index: int, line_index: int, pattern: str):
    """Function that will check around the "X" for specific pattern

    Args:
        data (list): data list
        data_index (int): index of current data line
        line_index (int): index inside the line
        pattern (str): pattern to match

    Returns:
        int: amout of xmas found
    """
    counter = 0
    counter += check_data(data, data_index, line_index, pattern)
    return counter


def count_xmas(data: list) -> int:
    """counts the amount of xmas in data

    Args:
        data (list): data list

    Returns:
        int: amout of xmas found
    """
    counter = 0
    for index, _ in enumerate(data):
        line = data[index]
        for i, _ in enumerate(line):
            if 'X' == line[i]:
                counter += check_around(data, index, i, "MAS")
        counter += check_line(line)

    return counter


#############################################
#                Part Two
#############################################

def check_around_part_two(data: list, data_index: int, line_index: int):
    """Counts the amous of X-MAS

    Args:
        data (list): data list
        data_index (int): line index
        line_index (int): index in the line

    Returns:
        int: amount of X-MAS
    """
    diag_up_left = ""
    diag_up_right = ""
    diag_down_left = ""
    diag_down_right = ""
    counter=0

    if data_index <= len(data)-2:
        if line_index >= 1:
            diag_down_left += data[data_index+1][line_index-1]
        if line_index <= len(data[0])-2:
            diag_down_right += data[data_index+1][line_index+1]
    if data_index >=1:
        if line_index >= 1:
            diag_up_left += data[data_index-1][line_index-1]
        if line_index <= len(data[0])-2:
            diag_up_right += data[data_index-1][line_index+1]
    if (diag_up_left == "M" and diag_down_right =="S") and (diag_up_right == "M" and diag_down_left =="S"):
        counter += 1
    if (diag_up_right == "M" and diag_down_left =="S") and (diag_down_right == "M" and diag_up_left =="S"):
        counter += 1
    if (diag_down_left == "M" and diag_up_right =="S") and (diag_up_left == "M" and diag_down_right =="S"):
        counter += 1
    if (diag_down_right == "M" and diag_up_left =="S") and (diag_down_left == "M" and diag_up_right =="S"):
        counter += 1
    return counter


def count_x_mas(data: list) -> int:
    """counts the amount of x-mas in data

    Args:
        data (list): data list

    Returns:
        int: amout of x-mas found
    """
    counter = 0
    for index, _ in enumerate(data):
        line = data[index]
        for i, _ in enumerate(line):
            if 'A' == line[i]:
                counter += check_around_part_two(data, index, i)
    return counter


if __name__ == "__main__":
    data_list = get_data()
    result = count_xmas(data_list)
    print(result)

    result_part_two = count_x_mas(data_list)
    print(result_part_two)
