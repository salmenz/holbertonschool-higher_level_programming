#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def val(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))

    def width(self):
        return self.__width

    def width(self, value):
        self.val("width", value)
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        self.val("height", value)
        self.__height = value

    def x(self):
        return self.__x

    def x(self, value):
        self.val("x", value)
        self.__x = value

    def y(self):
        return self.__y

    def y(self, value):
        self.val("y", value)
        self.__y = value
