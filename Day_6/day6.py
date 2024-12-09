#!/usr/bin/env python

"""
Filename: day6.py
Author: Nero
Description:
Usage:
"""

INPUT_FILE = "Day_6/input.txt"


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



if __name__ == "__main__":
    data_list = get_data()

