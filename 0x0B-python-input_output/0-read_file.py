#!/usr/bin/python3
"""
Program that prints a text file to stdout
"""


def read_file(filename=""):
    """ prints file contents """
    if filename == "":
        return
    with open(filename, "r") as f:
        print(f.read(), end="")
