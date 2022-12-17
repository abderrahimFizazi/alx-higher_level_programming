#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        l[idx] = element
    return l
