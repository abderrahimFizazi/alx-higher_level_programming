#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for a in my_list:
            if a == my_list[idx]:
                my_list.remove(a)
        return my_list
