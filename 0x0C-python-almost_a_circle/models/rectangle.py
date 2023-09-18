#!/usr/bin/python3
"""inherits Base"""
from base import Base


class Rectangle(Base):
    """Ractangle inherit Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method for width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self) -> int or float:
        """returns the are of a rectangle"""
        return self.__width * self.__height

    def display(self) -> None:
        """print the representation of a rectangle"""
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            for j in range(self.__x):
                print(" ", end='')
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """string representatio of a rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            width = "self.__width"
            height = "self.__height"
            list = ["self.id", width, height, "self.__x", "self.__y"]
            for val, name in zip(args, list):
                setattr(self, name, val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of the object(rectanle)"""
        my_dict = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
        return my_dict
