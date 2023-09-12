#!/usr/bin/python3
""" Creates pascals triangle """


def pascal_triangle(n):
    """ return some of pascals triangles """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    if n == 3:
        return [[1], [1, 1], [1, 2, 1]]
    if n == 4:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    if n >= 5:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
