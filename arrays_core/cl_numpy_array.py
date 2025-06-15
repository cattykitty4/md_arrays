import numpy as np
import doctest


class Array:
    def __init__(self, y_axis: int = 1, x_axis: int = 1, filler: int = 1, pair_arg=None):
        """
        Creating and preparing the Array class for work
        :param y_axis: define depth of y-coordinate array
        :param x_axis: define depth of x-coordinate array
        :param filler: number that fills numpy array
        :param pair_arg: this type of input allows to set XY-axis as one parameter

        Examples:
        >>> cor_new_array = Array(5, 5)              # correct way to create class
        >>> new_array_tuple = Array(pair_arg=(2, 5)) # correct way to create class with tuple
        >>> incor_new_array = Array('5', '5')        # incorrect way to create class
        Traceback (most recent call last):
        ...
        TypeError: Input number should be integer, not string!
        """
        if not isinstance(filler, (int, float)):
            raise TypeError('Input number should be integer, not string!')
        self.filler = filler

        if not isinstance(y_axis, (int, float)) or not isinstance(x_axis, (int, float)):
            raise TypeError('Input number should be integer, not string!')
        self.y_axis = y_axis
        self.x_axis = x_axis

        if not isinstance(pair_arg, (tuple, list)):
            self.pair_arg = None
        else:
            self.y_axis = pair_arg[0]
            self.x_axis = pair_arg[1]

    def __str__(self):
        return (f'This class can create any multidimensional arrays. You can set dimension of arrays by two ways\n'
                f'1. keyword. Just write "pair_arg=(y,x) and write any non below zero values instead x and y\n'
                f'2. Write Y-axis and X-axis in arguments. Example: Array(2, 4)\n\n'
                f'Also you can set the filler number in arrays by third argument.')

    def __repr__(self):
        return f'new_array = {self.__class__.__name__}{self.y_axis, self.x_axis}'

    def filled_with_zeros(self):
        """
        :return: return multidimensional array filled with zeros
        """
        zeros_array = np.zeros((self.y_axis, self.x_axis), dtype=int)
        return f'{zeros_array}\nAxis Y: {self.y_axis}, Axis X: {self.x_axis}'

    def filled_with_ones(self):
        """
        :return: return multidimensional array filled with ones
        """
        ones_array = np.ones((self.y_axis, self.x_axis), dtype=int)
        return f'{ones_array}\nAxis Y: {self.y_axis}, Axis X: {self.x_axis}'

    def filled_with_numbers(self):
        """
        :return: return multidimensional array filled with any self.filler amounts
        """
        numbers_array = np.full((self.y_axis, self.x_axis), self.filler, dtype=int)
        return f'{numbers_array}\nAxis Y: {self.y_axis}, Axis X:{self.x_axis}'


doctest.testmod()
