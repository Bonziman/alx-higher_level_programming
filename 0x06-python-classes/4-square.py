class Square:
    """Represents a Square."""

    def __init__(self, size=0):
        """Initializes a Square with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            It must be a non-negative integer.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size
