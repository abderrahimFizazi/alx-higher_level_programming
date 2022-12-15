#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if "{:c}".format(a) == 'e' or "{:c}".format(a) == 'q':
        continue
    else:
        print("{:c}".format(a), end='')
