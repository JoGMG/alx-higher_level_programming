#!/usr/bin/python3
""" Defines a function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ A function that finds a peak in a list of unsorted integers. """

    if list_of_integers == []:
        return None
    d_list = list_of_integers
    length = len(d_list)
    index = int(length / 2)

    if d_list[index - 1] < d_list[index] > d_list[index + 1]:
        return d_list[index]
    if d_list[index] == d_list[index - 1] == d_list[index + 1]:
        return d_list[index] if index < 2 else find_peak(d_list[:index])
    if index == 1 and d_list[index] < d_list[index - 1]:
        return d_list[index - 1]

    if d_list[index + 1] > d_list[index - 1]:
        return find_peak(d_list[index:])
    return find_peak(d_list[:index])
