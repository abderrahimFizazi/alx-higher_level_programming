#!/usr/bin/python3
def uppercase(str):
    for a in str:
        s = ord(a)
        if s > 96 and s < 123:
            s = ord(a) -32
        print("{:c}".format(s), end='')
    print('')
