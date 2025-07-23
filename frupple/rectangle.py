"""
Rectangle and Square geometric figures.
"""

import math
from .base import Figure


class Rectangle(Figure):
    """A rectangle figure."""
    
    def __init__(self, width: float, height: float):
        """Initialize a rectangle.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
            
        Raises:
            ValueError: If width or height is negative
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def diagonal(self) -> float:
        """Calculate the diagonal of the rectangle."""
        return math.sqrt(self.width ** 2 + self.height ** 2)


class Square(Rectangle):
    """A square figure (special case of rectangle)."""
    
    def __init__(self, side: float):
        """Initialize a square.
        
        Args:
            side: The side length of the square
            
        Raises:
            ValueError: If side is negative
        """
        super().__init__(side, side)
        self.side = side