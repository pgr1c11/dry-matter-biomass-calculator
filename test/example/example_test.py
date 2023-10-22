import pytest
from pytest import approx
import numpy as np
import pandas as pd
from src.example import multiply_numbers, multiply_number_array

def test_multiply_numbers() -> None:
  assert approx(multiply_numbers(np.float64(2.0), np.float64(5.0))) == 10.0

def test_multiply_number_array() -> None:
  df = pd.read_csv("data/example_data.csv", sep=',', header=0)
  numbers = df['Column B'].values
  assert multiply_number_array(numbers) == approx(39916800.0, abs=1e-12)
  print("Awesome! My test passed and I can read the console output")
