#!/usr/bin/python3

def find_peak(list_of_integers):
    """ A function that finds a peak in a list of unsorted integers. """
    if list_of_integers == []:
        return None
    d_list = list_of_integers
    length = len(d_list)
    index = int(length / 2)
    # print(index)
    # print("full list length: {}".format(fl_length))
    # print("full list index: {}".format(fl_index))
    # fh_list = fl[:fl_index]
    # print(fh_list)
    # fh_list_length = len(fh_list)
    # fh_list_index = int(fh_list_length / 2)
    # print(fh_list_length)
    # print(fh_list_index)

    if d_list[index - 1] < d_list[index] > d_list[index + 1]:
        return d_list[index]
    if index < 2 and d_list[index] == d_list[index - 1]:
        return d_list[index]
    if d_list[index] == d_list[index - 1] == d_list[index + 1]:
        return d_list[index] if d_list[index + 2] <= d_list[index] else find_peak(d_list[:index])
    if index == 1 and d_list[index] < d_list[index - 1]:
        return d_list[index - 1]
    # elif d_list[index] < d_list[index + 1] > d_list[index - 1]:
    #     return d_list[index + 1]
    
    if d_list[index + 1] > d_list[index - 1]:
        # print(d_list[index:])
        return find_peak(d_list[index:])
    # print(d_list[:index])
    return find_peak(d_list[:index])
    
