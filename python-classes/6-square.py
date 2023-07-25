#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Instantiation with optional size and optional position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size 
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or 
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Get/Set a current size of square"""
        return (self.__size)

    """property setter that sets the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
           print("")
           return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print('#', end="") for j in range(self.__size)]
            print("")
