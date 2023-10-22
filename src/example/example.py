from functools import reduce
import numpy as np
import numpy.typing as npt
from typing import Callable

def multiply_numbers(a: np.float64, b: np.float64) -> np.float64:
  return a * b

def multiply_number_array(numbers: npt.NDArray[np.float64]) -> np.float64:
  multiply: Callable[[np.float64, np.float64], np.float64] = lambda x, y: x * y
  return reduce(multiply, numbers, np.float64(1.0))
  