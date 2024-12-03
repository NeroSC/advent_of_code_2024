#!/usr/bin/env python

"""
Filename: day2.py
Author: Nero
Description:
Usage:
"""

INPUT_FILE = "input.txt"


def is_report_safe(report: list):
    """Checks if report is safe

    Args:
        report (list): List of value in a report

    Returns:
        bool: True if safe, False if unsafe
    """
    increase = all(report[index] < report[index+1] for index in range(len(report) - 1))
    decrease = all(report[index] > report[index+1] for index in range(len(report) - 1))

    if not (increase or decrease):
        return False

    for index in range(len(report) - 1):
        diff = abs(report[index] - report[index+1])
        if 1 > diff or diff > 3:
            return False
    return True


def can_report_be_safe(report: list):
    """Checks if reports can be safe if tampered

    Args:
        report (list): list of values of a report

    Returns:
        bool: true if safe false if not
    """
    if is_report_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_report_safe(modified_report):
            return True
    return False


def get_safe_reports(file: str = INPUT_FILE):
    """Gets lists of reports from input file

    Args:
        file (str, optional): Path to File. Defaults to INPUT_FILE.

    Returns:

    """
    _safe_reports = 0
    _unsafe_reports = 0

    with open(file, mode="r", encoding="utf-8") as input_file:
        for line in input_file:
            report_value_list = list(map(int, line.strip("\n").split()))
            if can_report_be_safe(report_value_list):
                _safe_reports += 1
            else:
                _unsafe_reports += 1
        return (_safe_reports, _unsafe_reports)


if __name__ == "__main__":
    safe_reports, unsafe_reports = get_safe_reports()
    print(safe_reports, unsafe_reports)
