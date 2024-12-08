#!/usr/bin/env python

"""
Filename: day3.py
Author: Nero
Description:
Usage:
"""

INPUT_FILE = "Day_5/input.txt"


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


def get_rules_and_updates(data: list):
    from collections import defaultdict
    sep = data.index("")
    rules = defaultdict(set)
    for i in data[:sep]:
        a, b = map(int, i.split("|"))
        rules[a].add(b)
    updates = [line.split(",") for line in data if "," in line]
    return rules, updates


# def get_order(rules: list):
#     ordered = []
#     for rule in rules:
#         order = [rule.split('|')[0], rule.split('|')[1]]
#         if len(ordered) == 0 or (order[0] not in ordered and order[1] not in ordered):
#             ordered += order
#         else:
#             if order[0] in ordered and order[1] not in ordered:
#                 ordered.insert(ordered.index(order[0])+1, order[1])
#             elif order[1] in ordered and order[0] not in ordered:
#                 ordered.insert(ordered.index(order[1]), order[0])
#             else:
#                 if ordered.index(order[1]) > ordered.index(order[0]):
#                     continue
#                 else:
#                     ordered.pop(ordered.index(order[0]))
#                     ordered.insert(ordered.index(order[1]), order[0])

#     return ordered


def check_updates_part_one(rules: dict, updates: list):
    good_updates = 0
    total = 0
    for update in updates:
        update = list(map(int, update))
        broken = 0
        for i, _ in enumerate(update):
            if broken == 1:
                break
            for j in range(i+1, len(update)):
                if update[j] not in rules[update[i]]:
                    broken = 1
                    break
        if broken == 0:
            good_updates += 1
            total += update[len(update) // 2]
    return good_updates, total


def check_updates_part_two(rules: dict, updates: list):
    good_updates = 0
    total = 0
    for update in updates:
        update = list(map(int, update))
        broken = 0
        for i, _ in enumerate(update):
            if broken == 1:
                break
            for j in range(i+1, len(update)):
                if update[j] not in rules[update[i]]:
                    broken = 1
                    break
        if broken == 0:
            good_updates += 1
            total += update[len(update) // 2]
    return good_updates, total


if __name__ == "__main__":

    data_list = get_data()
    rules_dict, updates_list = get_rules_and_updates(data_list)
    good_updates_total, result = check_updates_part_one(rules_dict, updates_list)
    print(good_updates_total, result)
    good_updates_total, result = check_updates_part_two(rules_dict, updates_list)
    print(good_updates_total, result)
