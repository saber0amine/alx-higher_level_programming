#!/usr/bin/python3
"""find a peak
"""


def find_peak(list_of_integers):
    """find peak in a list of integer
    """
    a = list_of_integers
    if a:
        if len(a) == 1:
            return a[0]
        if a[0] > a[1]:
            return a[0]
        if a[len(a) - 1] > a[len(a) - 2]:
            return a[len(a) - 1]
        m = len(a) // 2
        if a[m - 1] > a[m]:
            return find_peak(a[0:m])
        if a[m + 1] > a[m]:
            return find_peak(a[m + 1:])
        return a[m]
