"""
Frupple - A simple geometric computation library
Version 3.0.0
"""

from .base import Figure
from .circle import Circle
from .rectangle import Rectangle, Square
from .triangle import Triangle
from .parallelogram import Parallelogram
from .rhombus import Rhombus
from .point import Point
from .line import Line
from .cylinder import Cylinder

__version__ = "3.0.0"

__all__ = [
    "Figure",
    "Circle", 
    "Rectangle",
    "Square",
    "Triangle",
    "Parallelogram",
    "Rhombus", 
    "Point",
    "Line",
    "Cylinder"
]