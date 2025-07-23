"""
Rhombus geometric figure.
"""

from typing import Optional
from .base import Figure


class Rhombus(Figure):
    """A rhombus figure (special case of parallelogram with all sides equal)."""
    
    def __init__(self, side: float, height: Optional[float] = None, diagonal1: Optional[float] = None, diagonal2: Optional[float] = None):
        """Initialize a rhombus.
        
        Args:
            side: The side length of the rhombus (all sides are equal)
            height: Optional height for area calculation using base * height
            diagonal1: Optional first diagonal length
            diagonal2: Optional second diagonal length
            
        Raises:
            ValueError: If side is negative or insufficient parameters for area calculation
        """
        if side < 0:
            raise ValueError("Side length cannot be negative")
        if height is not None and height < 0:
            raise ValueError("Height cannot be negative")
        if diagonal1 is not None and diagonal1 < 0:
            raise ValueError("Diagonal1 cannot be negative")
        if diagonal2 is not None and diagonal2 < 0:
            raise ValueError("Diagonal2 cannot be negative")
        
        self.side = side
        self.height = height
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    
    def area(self) -> float:
        """Calculate the area of the rhombus.
        
        Uses diagonals if both are provided, otherwise uses side * height.
        
        Raises:
            ValueError: If insufficient parameters are provided for area calculation
        """
        if self.diagonal1 is not None and self.diagonal2 is not None:
            return 0.5 * self.diagonal1 * self.diagonal2
        elif self.height is not None:
            return self.side * self.height
        else:
            raise ValueError("Either both diagonals or height must be provided for area calculation")
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the rhombus."""
        return 4 * self.side