"""
Point utility class.
"""

import math


class Point:
    """A point in 2D space."""
    
    def __init__(self, x: float, y: float):
        """Initialize a point.
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        self.x = x
        self.y = y
    
    def distance_to(self, other: 'Point') -> float:
        """Calculate distance to another point.
        
        Args:
            other: Another Point object
            
        Returns:
            The Euclidean distance between the points
        """
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"