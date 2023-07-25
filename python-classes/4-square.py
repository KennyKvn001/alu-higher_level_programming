#!/usr/bin/pyhton3
"""Define a class Square"""


class Square:
    """Instantiation with optional size"""
    def __init__(self, size=0):
        self.__size = size
    @property
    def size(self):
        return self.__size
    """property setter that sets the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        return (self.__size ** 2)
