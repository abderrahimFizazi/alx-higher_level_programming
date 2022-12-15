#!/usr/bin/python3
def uppercase(str):
    for a in str:
        s = a
        if ord(a) > 96 and ord(a) < 123:
            s = ord(a) -32
        print("{:c}".format(s, end='')
    print("")
