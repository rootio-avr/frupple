"""
3D Cylinder geometric figure.
"""

import math


class Cylinder:
    """A 3D cylinder."""
    
    def __init__(self, radius: float, height: float):
        """Initialize a cylinder.
        
        Args:
            radius: The radius of the cylinder base
            height: The height of the cylinder
            
        Raises:
            ValueError: If radius or height is negative
        """
        if radius < 0 or height < 0:
            raise ValueError("Radius and height cannot be negative")
        self.radius = radius
        self.height = height
    
    def volume(self) -> float:
        """Calculate the volume of the cylinder."""
        return math.pi * self.radius ** 2 * self.height
    
    def surface_area(self) -> float:
        """Calculate the surface area of the cylinder."""
        return 2 * math.pi * self.radius * (self.radius + self.height)