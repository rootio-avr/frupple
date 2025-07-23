"""
Frupple - A simple geometric computation library
Version 1.0.0
"""

import math
from abc import ABC, abstractmethod
from typing import Optional

__version__ = "1.0.0"


class Figure(ABC):
    """Abstract base class for all geometric figures."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the figure."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the figure."""
        pass


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


class Triangle(Figure):
    """A triangle figure."""
    
    def __init__(self, base: float, height: float, side1: Optional[float] = None, side2: Optional[float] = None):
        """Initialize a triangle.
        
        Args:
            base: The base of the triangle
            height: The height of the triangle
            side1: Optional first side length for perimeter calculation
            side2: Optional second side length for perimeter calculation
            
        Raises:
            ValueError: If base or height is negative
        """
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self) -> float:
        """Calculate the area of the triangle."""
        return 0.5 * self.base * self.height
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle."""
        if self.side1 is None or self.side2 is None:
            raise ValueError("All three sides must be provided to calculate perimeter")
        return self.base + self.side1 + self.side2


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
