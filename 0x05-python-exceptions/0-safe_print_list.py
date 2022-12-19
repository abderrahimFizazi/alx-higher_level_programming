#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    summ = 0
    for i in range(0,x):
        try:
            summ = summ * 10 + my_list[i]
        except:
            print(summ)
            return i
    print(summ)
    return i+1
