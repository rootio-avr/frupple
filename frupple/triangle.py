"""
Triangle geometric figure.
"""

import math
from typing import Optional
from .base import Figure


class Triangle(Figure):
    """A triangle figure."""

    def __init__(
        self,
        base: float,
        height: Optional[float] = None,
        side2: Optional[float] = None,
        side3: Optional[float] = None,
    ):
        """Initialize a triangle.

        Args:
            base: The base of the triangle
            side2: Optional second side of the triangle
            side3: Optional third side of the triangle
            height: Optional height corresponding to the base

        Note:
            Either provide all three sides (base, side2, side3) OR
            provide base with height and at least one other side (side2 or side3)

        Raises:
            ValueError: If parameters are invalid or insufficient for triangle construction
        """
        if base < 0:
            raise ValueError("Base cannot be negative")
        if side2 is not None and side2 < 0:
            raise ValueError("Side2 cannot be negative")
        if side3 is not None and side3 < 0:
            raise ValueError("Side3 cannot be negative")
        if height is not None and height < 0:
            raise ValueError("Height cannot be negative")

        # Validate that we have sufficient information
        if side2 is not None and side3 is not None:
            # All three sides provided - check triangle inequality
            if base + side2 <= side3 or base + side3 <= side2 or side2 + side3 <= base:
                raise ValueError(
                    "Triangle inequality violated: sum of any two sides must be greater than the third"
                )
        elif height is not None and (side2 is not None or side3 is not None):
            # Height with at least one other side - valid
            pass
        else:
            raise ValueError(
                "Either provide all three sides OR provide base with height and at least one other side"
            )

        self.base = base
        self.side2 = side2
        self.side3 = side3
        self.height = height

    def area(self) -> float:
        """Calculate the area of the triangle.

        Uses height if provided, otherwise uses Heron's formula with all three sides.
        """
        if self.height is not None:
            return 0.5 * self.base * self.height
        elif self.side2 is not None and self.side3 is not None:
            # Use Heron's formula
            s = (self.base + self.side2 + self.side3) / 2
            return math.sqrt(s * (s - self.base) * (s - self.side2) * (s - self.side3))
        else:
            raise ValueError("Cannot calculate area: insufficient parameters")

    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle.
        
        Can calculate with either all three sides OR with height and two sides.

        Raises:
            ValueError: If insufficient parameters are provided
        """
        if self.side2 is not None and self.side3 is not None:
            # All three sides provided
            return self.base + self.side2 + self.side3
        elif self.height is not None and self.side2 is not None:
            # Calculate third side using Pythagorean theorem or law of cosines
            # For simplicity, assume it's a right triangle with height perpendicular to base
            third_side = math.sqrt(self.side2**2 - self.height**2) if self.side2 > self.height else math.sqrt(self.height**2 + self.base**2)
            return self.base + self.side2 + third_side
        elif self.height is not None and self.side3 is not None:
            # Calculate second side using similar logic
            second_side = math.sqrt(self.side3**2 - self.height**2) if self.side3 > self.height else math.sqrt(self.height**2 + self.base**2)
            return self.base + second_side + self.side3
        else:
            raise ValueError("Need either all three sides OR height with two sides to calculate perimeter")
