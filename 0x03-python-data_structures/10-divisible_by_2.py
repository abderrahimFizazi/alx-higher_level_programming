#!/usr/bin/pytho3
def divisible_by_2(my_list=[]):
    new_l = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            new_l.append(True)
        else:
            new_l.append(False)
    return new_l
