#!/usr/bin/env python

"""
Filename: day6.py
Author: Nero
Description:
Usage:
"""

import pprint
INPUT_FILE = "Day_7/input.txt"


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

def test_values_part_one(data):
    total=0
    for line in data:
        sep=line.split(":")
        value=int(sep[0])
        numbers=list(map(int,sep[1].split()))
        possibles=[numbers.pop(0)]
        while numbers:
            temp=[]
            current=numbers.pop(0)
            for p in possibles:
                temp.append(p+current)
                temp.append(p*current)
            possibles=temp
        if value in possibles:
            total+=value
    return total

def test_values_part_two(data):
    total=0
    for line in data:
        sep=line.split(":")
        value=int(sep[0])
        numbers=list(map(int,sep[1].split()))
        possibilities=[numbers.pop(0)]
        while numbers:
            temp=[]
            current=numbers.pop(0)
            for p in possibilities:
                temp.append(p+current)
                temp.append(p*current)
                temp.append(int(str(p)+str(current)))
            possibilities=temp
        if value in possibilities:
            total+=value
    return total



if __name__ == "__main__":
    data_list = get_data()
    print(test_values_part_one(data_list))
    print(test_values_part_two(data_list))
