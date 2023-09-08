#!/usr/bin/python3
""" Defines a function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ A function that finds a peak in a list of unsorted integers. """
    
    d_list = list_of_integers
    if d_list is None or d_list == []:
        return None
    
    l_len = len(d_list)
    mid_index = int(l_len / 2)

    if l_len == 1:
        return d_list[0]
    if l_len == 2:
        return max(d_list)
    if d_list[mid_index - 1] <= d_list[mid_index] >= d_list[mid_index + 1]:
        return d_list[mid_index]

    if mid_index > 0 and d_list[mid_index] < d_list[mid_index + 1]:
        return find_peak(d_list[mid_index:])
    if mid_index > 0 and d_list[mid_index] < d_list[mid_index - 1]:
        return find_peak(d_list[:mid_index])

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
