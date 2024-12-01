#!/usr/bin/env python

"""
Filename: day1.py
Author: Nero
Description:
Usage:
"""
import re

INPUT_FILE = "input.txt"


def get_location_id_lists(file: str = INPUT_FILE):
    """Gets sorted column lists from input file

    Args:
        file (str, optional): Path to File. Defaults to INPUT_FILE.

    Returns:
        tuple (list,list): sorted location Id lists
    """
    with open(file, mode="r", encoding="utf-8") as input_file:
        lines = input_file.read()
    matches = re.findall(r"(\w+)\s+(\w+)", lines)

    location_id_list_1 = [int(match[0]) for match in matches]
    location_id_list_2 = [int(match[1]) for match in matches]
    return sorted(location_id_list_1), sorted(location_id_list_2)


def get_distances_sum(list_A: list, list_B: list):
    """Calculates the sum of distances

    Args:
        list_A (list): first column
        list_B (list): second column

    Returns:
        int: distances sum
    """
    distances = []
    for i in range(len(list_A)):
        distances.append(abs(list_A[i]-list_B[i]))
    return sum(distances)


def find_similarities(list_A: list, list_B: list):
    """_summary_

    Args:
        list_A (list): _description_
        list_B (list): _description_

    Returns:
        _type_: _description_
    """
    similarities=[]
    for i in list_A:
        multiplier=list_B.count(i)
        similarities.append(i*multiplier)
    return sum(similarities)

if __name__ == "__main__":
    location_id_A, location_id_B = get_location_id_lists()
    result = get_distances_sum(location_id_A, location_id_B)
    print(result)
    result = find_similarities(location_id_A,location_id_B)
    print(result)
