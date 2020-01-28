#!/usr/bin/python3
"""
class Rectangle
that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle - class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for rectangle
        Arguments:
        @width: width of the rectangle
        @height: height of the rectangle
        @x: position in x
        @y: position in y
        @id: amount of instances created
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def val(self, name, value):
        """
        Checks the values passed into Rectangle
        instantation for validity
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.val("width", value)
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.val("height", value)
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.val("x", value)
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.val("y", value)
        self.__y = value

    def display(self):
        """Prints the current rectangle #"""
        print("\n" * self.y, end="")
        for rows in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """
        formats string representation of the Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes of Rectangle:
        Argument 1: id
        Argument 2: width
        Argument 3: height
        Argument 4: x
        Argument 5: y
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation of
        a rectangle object."""
        dic = dict()
        dic['id'] = self.id
        dic['width'] = self.width
        dic['height'] = self.height
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
