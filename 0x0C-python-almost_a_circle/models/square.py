#!/usr/bin/python3
"""
This module for class, Square,
inherited from Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square - class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for square
        Arguments:
        @size: size of the rectangle
        @x: position in x
        @y: position in y
        @id: amount of instances created
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """
        formats string representation of the Square
        """
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates attributes of Square objects:
        Argument 1: id
        Argument 2: size
        Argument 3: x
        Argument 4: y
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.width = args[1]
                self.height = args[1]
            if i == 2:
                self.x = args[2]
            if i == 3:
                self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of
        a Square object."""
        dic = dict()
        dic['id'] = self.id
        dic['size'] = self.width
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
