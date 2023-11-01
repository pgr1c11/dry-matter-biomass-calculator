from typing import List
import numpy as np
from scipy.stats import truncnorm


def stack_arrays(arrays: List[np.ndarray]) -> np.ndarray:
    """Stack a list of arrays on top of each other (axis = 0)

    Args:
        arrays (List[np.ndarray]): List of arrays. Must have same number of columns.

    Returns:
        np.ndarray: Stacked arrays.
    """
    return np.concatenate(arrays)


def repeat_single(shape: tuple, value: float) -> np.ndarray:
    """Repeat a single value to form an array of a defined shape

    Args:
        shape (tuple): Shape (rows, columns)
        value (float): Value to be repeated

    Returns:
        np.ndarray
    """
    _: np.ndarray = np.empty(shape=shape)
    _[:] = value
    return _


def repeat_single_bool(shape: tuple, value: bool) -> np.ndarray:
    """Repeat a single boolean value to form an array of a defined shape

    Args:
        shape (tuple): Shape (rows, columns)
        value (bool): Bool value to be repeated

    Returns:
        np.ndarray
    """
    _: np.ndarray = np.full(shape=shape, fill_value=value)
    return _


def repeat_2d_array_as_columns(iters: int, array: np.ndarray) -> np.ndarray:
    """Repeat a 2d numpy array horizontally as columns

    Args:
        iters (int): Iterations.
        array (np.ndarray): Array to repeat.

    Returns:
        np.ndarray
    """
    stack: np.ndarray = np.hstack([array for _ in range(iters)])
    return stack


def repeat_2d_array_as_rows(iters: int, array: np.ndarray) -> np.ndarray:
    """Repeat a 2d numpy array vertically as rows

    Args:
        iters (int): Iterations.
        array (np.ndarray): Array to repeat.

    Returns:
        np.ndarray
    """
    stack: np.ndarray = np.vstack([array for _ in range(iters)])
    return stack


def repeat_1d_array_as_columns(iters: int, column: np.ndarray) -> np.ndarray:
    """Repeat a column (np.ndarray) to form an array of a defined shape

    Args:
        iters (int): How many times the column (np.ndarray) should be repeated
        column (np.ndarray): The column (np.ndarray) to be repeated

    Returns:
        np.ndarray
    """
    stack = np.vstack([column for _ in range(iters)])
    return stack.transpose()


def repeat_1d_array_as_rows(iters: int, row: np.ndarray) -> np.ndarray:
    """Repeat a row (np.ndarray) to form an array of a defined shape

    Args:
        iters (int): How many times the row (np.ndarray) should be repeated
        row (np.ndarray): The row (np.ndarray) to be repeated

    Returns:
        np.ndarray
    """
    return np.vstack([row for _ in range(iters)])


def discrete_uniform_1d(shape: tuple, low: float, high: float) -> np.ndarray:
    """Sample from a discrete uniform distribution and produce an array of a specified shape.
    All rows in a specified column will have the same sample value, but each column will be different (1 dimensional variability).

    Args:
        shape (tuple): Shape (rows, columns)
        low (float): Lower bound of the discrete uniform distribution to be sampled
        high (float): Upper bound of the discrete uniform distribution to be sampled

    Returns:
        np.ndarray
    """
    row = np.random.uniform(low=low, high=high, size=shape[1])
    arr = repeat_1d_array_as_rows(iters=shape[0], row=row)
    return arr


def discrete_uniform_2d(shape: tuple, low: float, high: float) -> np.ndarray:
    """Sample from a discrete uniform distribution and produce an array of a specified shape.
    All rows and columns contain different sample values (2 dimensional variability).

    Args:
        shape (tuple): Shape (rows, columns)
        low (float): Lower bound of the discrete uniform distribution to be sampled
        high (float): Upper bound of the discrete uniform distribution to be sampled

    Returns:
        np.ndarray: _description_
    """
    return np.random.uniform(low=low, high=high, size=shape)


def triangular_1d(shape: tuple, low: float, high: float, mode: float) -> np.ndarray:
    """Sample from a triangular distribution and produce an array of a specified shape.
    All rows in a specified column will have the same sample value, but each column will be different (1 dimensional variability).  
    
    Args:
        shape (tuple): Shape (rows, columns)
        low (float): Lower bound of the triangular distribution to be sampled
        high (float): Upper bound of the triangular distribution to be sampled
        mode (float): Mode of the triangular distribution to be sampled

    Returns:
        np.ndarray
    """
    row = np.random.triangular(left=low, mode=mode, right=high, size = shape[1])
    arr = repeat_1d_array_as_rows(iters=shape[0], row=row)
    return arr


def triangular_2d(shape: tuple, low: float, high: float, mode: float) -> np.ndarray:
    """Sample from a triangular distribution and produce an array of a specified shape.
    All rows and columns contain different sample values (2 dimensional variability).

    Args:
        shape (tuple): Shape (rows, columns)
        low (float): Lower bound of the triangular distribution to be sampled
        high (float): Upper bound of the triangular distribution to be sampled
        mode (float): Mode of the triangular distribution to be sampled

    Returns:
        np.ndarray
    """
    return np.random.triangular(left=low, mode=mode, right=high, size = shape)


def normal_1d(shape: tuple, mu: float, sigma: float) -> np.ndarray:
    """Sample from a normal distribution and produce an array of a specified shape.
    All rows in a specified column will have the same sample value, but each column will be different (1 dimensional variability).
    
    Args:
        shape (tuple): Shape (rows, columns)
        mu (float): Mean of the normal distribution to be sampled
        sigma (float): Standard deviation of the normal distribution to be sampled

    Returns:
        np.ndarray
    """
    row = np.random.normal(loc=mu, scale=sigma, size=shape[1])
    arr = repeat_1d_array_as_rows(iters=shape[0],row=row)
    return arr


def normal_2d(shape: tuple, mu: float, sigma: float) -> np.ndarray:
    """Sample from a normal distribution and produce an array of a specified shape.
    All rows and columns contain different sample values (2 dimensional variability).

    Args:
        shape (tuple): Shape (rows, columns)
        mu (float): Mean of the normal distribution to be sampled
        sigma (float): Standard deviation of the normal distribution to be sampled

    Returns:
        np.ndarray
    """
    return np.random.normal(loc=mu, scale=sigma, size=shape)


def truncated_normal_1d(shape: tuple, mu: float, sigma: float, low: float, high: float) -> np.ndarray:
    """Sample from a truncated normal distribution and produce an array of a specified shape.
    All rows in a specified column will have the same sample value, but each column will be different (1 dimensional variability).

    Args:
        shape (tuple): Shape (rows, columns)
        mu (float): Mean of the normal distribution to be sampled
        sigma (float): Standard deviation of the normal distribution to be sampled
        low (float): Lower bound of the normal distribution to be sampled
        high (float): Upper bound of the normal distribution to be sampled

    Returns:
        np.ndarray
    """
    a, b = (low - mu) / sigma, (high - mu) / sigma
    row: np.ndarray = truncnorm.rvs(a=a,b=b,loc=mu,scale=sigma, size=shape[1])
    arr: np.ndarray = repeat_1d_array_as_rows(iters=shape[0], row=row)
    return arr


def truncated_normal_2d(shape: tuple, mu: float, sigma: float, low: float, high: float) -> np.ndarray:
    """Sample from a truncated normal distribution and produce an array of a specified shape.
    All rows and columns contain different sample values (2 dimensional variability).

    Args:
        shape (tuple): Shape (rows, columns)
        mu (float): Mean of the normal distribution to be sampled
        sigma (float): Standard deviation of the normal distribution to be sampled
        low (float): Lower bound of the normal distribution to be sampled
        high (float): Upper bound of the normal distribution to be sampled

    Returns:
        np.ndarray
    """
    a, b = (low - mu) / sigma, (high - mu) / sigma
    _: np.ndarray = truncnorm.rvs(a=a,b=b,loc=mu,scale=sigma, size=shape)
    return _


def plus_minus_uncertainty_to_normal_1d(value: float, uncertainty: float, n_sds: float, shape: tuple) -> np.ndarray:
    """Return a normally distributed sample given a value and uncertainty expressed as +/- a percentage. 
    For a 95% confidence interval set n_sds to 1.96. 
    All rows in a specified column will have the same sample value, but each column will be different (1 dimensional variability).

    This function has been written to serve Table 5.5b on Page 5.32, Tier 2 Steady State Method for Mineral Soils, Chapter 5 Cropland,
    2019 Refinement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories. Table 5.5b notes:
        
        "Uncertainty is assumed to be ±75% for the N content estimates and ±50% for the lignin content estimates, expressed as a 95%
        confidence intervals."

    This function also serves Table 11.2 on Page 11.19, Tier 2 Steady State Method for Mineral Soils, Chapter 11 N2O Emissions from
    Managed Soils, and CO2 Emissions from Lime and Urea Application, 2019 Refinement to the 2006 IPCC Guidelines for National Greenhouse
    Gas Inventories. 

    Args:
        value (float): Reported value
        uncertainty (float): Uncertainty expressed as +/- a percentage.
        n_sds (float): Number of standard deviations which the uncertainty represents.
        shape (tuple): Shape (rows, columns)

    Returns:
        np.ndarray
    """
    sigma=(value*(uncertainty/100))/n_sds
    mu=value
    return normal_1d(shape=shape, mu=mu, sigma=sigma)


def grouped_avg(my_array: np.ndarray, n: int = 12) -> np.ndarray:
    """ Row-wise averaging of numpy arrays. For example:
    1   2   3
    4   5   6
    7   8   9
    10  11  12
    13  14  15
    16  17  18

    if n = 6, becomes:
    8.5 9.5 10.5

    because:
    (1 + 4 + 7 + 10 + 13 + 16) / 6 = 8.5
    (2 + 5 + 8 + 11 + 14 + 17) / 6 = 9.5
    etc.

    if n = 2, becomes:
    2.5  3.5  4.5
    8.5  9.5  10.5
    14.5 15.5 16.5

    because:
    (in column 0) (1 + 4) / 2 = 2.5, (7 + 10) / 2 = 8.5, (13 + 16) / 2 = 14.5
    (in column 1) (2 + 5) / 2 = 3.5, (8 + 11) / 2 = 9.5, (14 + 17) / 2 = 15.5

    Source: https://stackoverflow.com/questions/30379311/fast-way-to-take-average-of-every-n-rows-in-a-npy-array

    Args:
        my_array (np.ndarray): Input array
        n (int, optional): Number of rows to average. Defaults to 12.

    Returns:
        np.ndarray: Output array
    """
    result = np.cumsum(my_array, 0)[n-1::n]/float(n)
    result[1:] = result[1:] - result[:-1]
    return result
