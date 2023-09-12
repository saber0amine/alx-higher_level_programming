#!/usr/bin/python3
"""
Program that writes text to a file
"""


def append_write(filename="", text=""):
    """ write to a file and return # of characters written """
    if filename == "":
        return
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
