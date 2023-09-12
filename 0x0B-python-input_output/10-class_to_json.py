#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
for JSON serialization of an obj
"""


def class_to_json(obj):
    """ returns dictionary desc """
    return vars(obj)
