"""
Parallelogram geometric figure.
"""

from typing import Optional
from .base import Figure


class Parallelogram(Figure):
    """A parallelogram figure."""
    
    def __init__(self, base: float, side: float, height: float, angle: Optional[float] = None):
        """Initialize a parallelogram.
        
        Args:
            base: The base length of the parallelogram
            side: The side length of the parallelogram
            height: The height of the parallelogram (perpendicular distance between parallel sides)
            angle: Optional angle between base and side in degrees (for perimeter calculation)
            
        Raises:
            ValueError: If base, side, or height is negative, or angle is invalid
        """
        if base < 0 or side < 0 or height < 0:
            raise ValueError("Base, side, and height cannot be negative")
        if angle is not None and (angle <= 0 or angle >= 180):
            raise ValueError("Angle must be between 0 and 180 degrees")
        
        self.base = base
        self.side = side
        self.height = height
        self.angle = angle
    
    def area(self) -> float:
        """Calculate the area of the parallelogram."""
        return self.base * self.height
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the parallelogram."""
        return 2 * (self.base + self.side)