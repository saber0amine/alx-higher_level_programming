#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """init square
        Args:
            size (int): square size.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets value into size, must be int.

        Args:
            value (int): square size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
        value (int): square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Sets value of position.

        Args:
            value (int): square position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets value into position.

        Args:
            value (int): square position.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calc area
        returns:
            return area.
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with #"""
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print()
            sqr_pattern = " " * self.__position[0] + "#" * self.__size + "\n"
            print(sqr_pattern * self.__size, end="")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
            
my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)