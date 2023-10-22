import pytest
from pytest import approx
import numpy as np

from src.example import square, rectangle, circle

def test_square_area() -> None:
  assert square(np.float64(3.0)) == approx(9.0, rel=1e-6)

def test_rectangle_area() -> None:
  assert rectangle(np.float64(2.0), np.float64(4.0)) == approx(8.0, rel=1e-6)

def test_circle_area() -> None:
  assert circle(np.float64(4.0)) == approx(50.26548, rel=1e-6)
