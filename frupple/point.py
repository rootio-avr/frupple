"""
Point utility class.
"""

import math
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .line import Line


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
    
    def distance_to(self, other: Union['Point', 'Line']) -> float:
        """Calculate distance to another point or line.
        
        Args:
            other: Another Point object or Line object
            
        Returns:
            The Euclidean distance between the points or 
            perpendicular distance from point to line
        """
        if hasattr(other, 'distance_to_point'):
            # It's a Line object
            return other.distance_to_point(self)
        else:
            # It's a Point object
            return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"