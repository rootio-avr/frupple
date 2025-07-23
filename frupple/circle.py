"""
Circle geometric figure.
"""

import math
from .base import Figure


class Circle(Figure):
    """A circle figure."""
    
    def __init__(self, radius: float):
        """Initialize a circle.
        
        Args:
            radius: The radius of the circle
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
    
    def diameter(self) -> float:
        """Calculate the diameter of the circle."""
        return 2 * self.radius