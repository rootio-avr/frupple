"""
Line geometric object.
"""

import math
from .point import Point


class Line:
    """A line defined by two points."""
    
    def __init__(self, point1: Point, point2: Point):
        """Initialize a line.
        
        Args:
            point1: First point defining the line
            point2: Second point defining the line
            
        Raises:
            ValueError: If both points are the same (cannot form a line)
        """
        if point1.x == point2.x and point1.y == point2.y:
            raise ValueError("Cannot create a line from two identical points")
        
        self.point1 = point1
        self.point2 = point2
    
    def length(self) -> float:
        """Calculate the length of the line segment."""
        return self.point1.distance_to(self.point2)
    
    def slope(self) -> float:
        """Calculate the slope of the line.
        
        Returns:
            The slope of the line
            
        Raises:
            ValueError: If the line is vertical (infinite slope)
        """
        if self.point2.x == self.point1.x:
            raise ValueError("Vertical line has infinite slope")
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
    
    def distance_to_point(self, point: Point) -> float:
        """Calculate the perpendicular distance from a point to this line.
        
        Args:
            point: The point to calculate distance to
            
        Returns:
            The perpendicular distance from the point to the line
        """
        # Using the formula: distance = |ax + by + c| / sqrt(a² + b²)
        # where the line equation is ax + by + c = 0
        
        # Convert two-point form to general form ax + by + c = 0
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        
        # Calculate distance
        numerator = abs(a * point.x + b * point.y + c)
        denominator = math.sqrt(a * a + b * b)
        
        return numerator / denominator
    
    def __repr__(self) -> str:
        return f"Line({self.point1}, {self.point2})"