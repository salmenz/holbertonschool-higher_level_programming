#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        if len(position) == 2 and type(position) == tuple and\
        type(position[0]) == int and position[0] >= 0 and\
        type(position[1]) == int and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        if len(value) == 2 and type(value) == tuple and\
        type(value[0]) == int and value[0] >= 0 and\
        type(value[1]) == int and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @proprety
    def position(self):
        return self.__position

    def my_print(self):
        if self.size == 0:
            print()
        elif self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
