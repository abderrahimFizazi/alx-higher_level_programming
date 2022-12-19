#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    summ = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            summ += 1
        except (TypeError, ValueError):
            continue
    print()
    return summ