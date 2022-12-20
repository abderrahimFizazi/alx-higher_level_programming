#!/usr/bin/python3
# 2-square.py by abdo
"""Defines a square """


class Square:
    """Initializing this square class
        Args: size - represnets the size of the square defined
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
