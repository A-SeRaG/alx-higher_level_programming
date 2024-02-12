#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base

class Rectangle (Base):
    '''Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of the rectangle'''
        return self.__width
    
    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value
    
    @property
    def height(self):
        '''Height of the rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value
    
    @property
    def x(self):
        '''x of the rectangle'''
        return self.__x
    
    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value
    
    @property
    def y(self):
        '''y of the rectangle'''
        return self.__y
    
    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value
    
    def validate_integer(self, name, value, flag = True):
        '''Method for validating the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if flag and value < 0:
            raise TypeError("{} must be >= 0".format(name))
        elif not flag and value <= 0:
            raise TypeError("{} must be > 0".format(name))
    
    def area(self):
        '''Method for calculate the area of the rectangle'''
        return self.height * self.width
    
    def display(self):
        '''Method to display the rectangle'''
        o = '\n' * self.y + \
        (' ' * self.x + '#' * self.width + '\n') * self.height
        print(o, end='')

    def __str__(self):
        '''Method returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return '[{}] ({}) {}/{} - {}/{}'.\
        format(type(self).__name__, self.id, self.x,self.y,\
               self.width, self.height)
    
    def update(self, id=None, width=None, height=None, x=None,y=None):
        '''Private Update method'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Method that assigns a key/value argument to attributes'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)