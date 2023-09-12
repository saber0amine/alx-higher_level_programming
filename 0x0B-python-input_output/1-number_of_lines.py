#!/usr/bin/python3
"""
Program that counts lines in a file
"""


def number_of_lines(filename=""):
    """ count lines in file """
    count = 0
    if filename == "":
        return count
    with open(filename, "r") as f:
        for l in f:
            count += 1
    return count
