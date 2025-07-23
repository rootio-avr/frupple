"""
Base classes for geometric figures.
"""

from abc import ABC, abstractmethod


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
