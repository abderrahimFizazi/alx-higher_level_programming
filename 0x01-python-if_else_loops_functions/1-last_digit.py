#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0: 
    lst = number % 10
else: 
    lst = number % -10
print(f"{'Last digit of '}{number}{' is '}{lst}{' and is '}",end='')
if lst > 5:
    print("greater than 5")
elif lst == 0:
    print("0")
else:
    print("less than 6 and not 0")
