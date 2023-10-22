import numpy as np

def square(side: np.float64) -> np.float64:
  return side * side

def rectangle(length: np.float64, width: np.float64) -> np.float64:
  return length * width

def circle(radius: np.float64) -> np.float64:
  return np.float64(np.pi * np.power(radius, 2.0))