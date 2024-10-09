class Array(object):
    """
	Class: arrays.py

	An Array is a restricted list whose clients can use
	only [], len, iter, and str.

	To instantiate, use

	     <arrayName> = Array(<capacity>, <optional fill value>)

	The fill value is None by default.
	"""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
       
        self.__items = list()
        
        for count in range(capacity):
            self.__items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.__items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.__items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self.__items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""

        """Python is tricky. Slicing automatically works with anything
        that is subscriptable unless we disable it. This disables it.
        Attempting to use slicing with an array results in an exception."""
        if isinstance(index, slice):
            raise TypeError("Array does not support slicing.")
        
        if not isinstance(index, int):
            raise TypeError("Array index must be an int.")
        
        if index < 0 or index >= len(self.__items):
            raise IndexError("Index out of range.")

        return self.__items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""

        if not isinstance(index, int):
            raise TypeError("Array index must be an int.")

        if index < 0 or index >= len(self.__items):
            raise IndexError("Index out of range.")

        self.__items[index] = newItem

class TwoDArray(object):
    """
    Class: TwoDArray

    A TwoDArray is a restricted 2-dimensional array whose clients can use
    only [row, col],  len, iter, and str.

    To instantiate, use

         <arrayName> = TwoDArray(<num_rows>, <num_cols>, <optional fill value>)

    The fill value is None by default.
    """

    def __init__(self, num_rows, num_cols, fillValue = None):
        """num_rows and num_cols are the dimensions of the array.
        fillValue is placed at each position."""
        
        self.__items = []
        self.__num_rows = num_rows
        self.__num_cols = num_cols
       
        for row in range(num_rows):
            self.__items.append([fillValue] * num_cols)

    def size(self):
        """-> A tuple containing the dimensions of the array (rows, columns)."""
       
        return (self.__num_rows, self.__num_cols)

    def __str__(self):
        """-> The string representation of the 2D array."""
        
        return '\n'.join(str(row) for row in self.__items)

    def __getitem__(self, index):
        """Subscript operator for access at [row, column]."""
        
        if not isinstance(index, tuple) or not isinstance(index[0], int) or not isinstance(index[1], int):
            raise TypeError("Index must be a tuple of two integers.")
        
        row, col = index
        if not (0 <= row < self.__num_rows and 0 <= col < self.__num_cols):
            raise IndexError("Index out of range.")
        
        return self.__items[row][col]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at [row, column]."""
        
        if not isinstance(index, tuple) or not isinstance(index[0], int) or not isinstance(index[1], int):
            raise TypeError("Index must be a tuple of two integers.")
        
        row, col = index
        if not (0 <= row < self.__num_rows and 0 <= col < self.__num_cols):
            raise IndexError("Index out of range.")
        
        self.__items[row][col] = newItem