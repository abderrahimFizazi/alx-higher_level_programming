#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_new = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            break
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        finally:
            my_new.append(res)
    return my_new
