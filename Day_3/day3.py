#!/usr/bin/env python

"""
Filename: day3.py
Author: Nero
Description:
Usage:
"""
import re
import math
INPUT_FILE = "input.txt"

#############################################
#                Part One
#############################################

REGEX_PART_ONE = r"(mul\(\d+,\d+\))"
REGEX_PART_TWO = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"


def mul(func: str) -> int:
    """Function that multiplies numbers in str "mul(XXX,XXX)"

    Args:
        func (str): ex: mul(XXX,XXX)

    Returns:
        int: return product
    """
    func = re.sub(r'mul', '', func)
    digits = list(map(int, func.strip('()').split(',')))
    return math.prod(digits)


def get_data(file: str = INPUT_FILE):
    """Function that gets data from file

    Args:
        file (str, optional): File. Defaults to INPUT_FILE.

    Returns:
        str: data
    """
    with open(file, mode="r", encoding="utf-8") as input_file:
        data = input_file.read()
    return data


def get_mul_list_part_one(data: str) -> list:
    """get all mul(XX,XX)

    Args:
        data (str): _description_

    Returns:
        list: list of all mul()
    """
    matches = re.finditer(REGEX_PART_ONE, data)
    mul_list = [mul(match.group()) for match in matches]

    return mul_list


def get_mul_list_part_two(data):
    """get all mul(XX,XX)

    Args:
        data (str): _description_

    Returns:
        list: list of all mul() based on dos and donts
    """
    do = 1
    mul_list = []
    matches = re.finditer(REGEX_PART_TWO, data)
    for match in matches:
        if match.group() == "don't()":
            do = 0
            continue
        if match.group() == "do()":
            do = 1
            continue
        if do == 1:
            mul_list.append(mul(match.group()))
    return mul_list


def sum_of_mul(mul_list: list) -> int:
    """sum of list

    Args:
        mul_list (list): list of mul()

    Returns:
        int: sum of products
    """
    return sum(mul_list)


#############################################
#                Part Two
#############################################

# def sum_of_mul_part_two()

if __name__ == "__main__":
    data = get_data()
    mul_list = get_mul_list_part_one(data)
    result = sum_of_mul(mul_list)
    print(result)
    mul_list = get_mul_list_part_two(data)
    result = sum_of_mul(mul_list)
    print(result)
