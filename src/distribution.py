import numpy as np
import src.builders as bd


class Distribution:
    """
    Distribution class for sampling values based on a defined distribution.

    This class provides a common interface for generating arrays of values based on a specific distribution.

    Methods:
        sample(shape: tuple, column_wise_sampling: bool) -> np.ndarray:
            Generate an array of sampled values based on the distribution.
    """
    def sample(self, shape: tuple, column_wise_sampling: bool) -> np.ndarray:
        """
        Generate an array of sampled values based on the distribution.

        Args:
            shape (tuple): The shape of the output array to be generated.
            column_wise_sampling (bool): If True, samples values column-wise; otherwise, samples randomly
                                         accross rows and columns.

        Returns:
            np.ndarray: An array of sampled values based on the distribution.

        Note:
            This method should be overridden in subclasses to provide the specific implementation of
            value sampling based on the desired distribution.
        """


class DiscreteUniform(Distribution):
    """
    DiscreteUniform class, a subclass of Distribution, for sampling values from a discrete uniform distribution.

    This class inherits from the Distribution class and provides a way to sample values from a discrete uniform distribution
    with a specified range.

    Attributes:
        low (float): The lower bound of the distribution range.
        high (float): The upper bound of the distribution range.
    """
    def __init__(self, low: float, high: float) -> None:
        self.low = low
        self.high = high

    def sample(self, shape: tuple, column_wise_sampling: bool) -> np.ndarray:
        """
        Generate an array of sampled values from a discrete uniform distribution.

        Args:
            shape (tuple): The shape of the output array to be generated.
            column_wise_sampling (bool): If True, samples values column-wise; otherwise, samples randomly
                                         accross rows and columns.

        Returns:
            np.ndarray: An array of sampled values from the discrete uniform distribution.
        """
        sample_function = (bd.discrete_uniform_1d
                           if column_wise_sampling
                           else bd.discrete_uniform_2d)
        _: np.ndarray = sample_function(shape=shape, low=self.low, high=self.high)
        return _


class Normal(Distribution):
    """
    Normal class, a subclass of Distribution, for sampling values from a normal distribution.

    This class inherits from the Distribution class and provides a way to sample values from a normal distribution
    with a specified mean and standard deviation.

    Attributes:
        mu (float): The mean of the normal distribution.
        sigma (float): The standard deviation of the normal distribution.
    """
    def __init__(self, mu: float, sigma: float) -> None:
        self.mu = mu
        self.sigma = sigma

    def sample(self, shape: tuple, column_wise_sampling: bool) -> np.ndarray:
        """
        Generate an array of sampled values from a normal distribution.

        Args:
            shape (tuple): The shape of the output array to be generated.
            column_wise_sampling (bool): If True, samples values column-wise; otherwise, samples randomly
                                         accross rows and columns.

        Returns:
            np.ndarray: An array of sampled values from the normal distribution.
        """
        sample_function = (bd.normal_1d
                           if column_wise_sampling
                           else bd.normal_2d)
        _: np.ndarray = sample_function(shape=shape, mu=self.mu, sigma=self.sigma)
        return _


class TruncatedNormal(Distribution):
    """
    TruncatedNormal class, a subclass of Distribution, for sampling values from a truncated normal distribution.

    This class inherits from the Distribution class and provides a way to sample values from a truncated normal distribution
    with specified parameters: mean, standard deviation, lower bound, and upper bound.

    Attributes:
        mu (float): The mean of the truncated normal distribution.
        sigma (float): The standard deviation of the truncated normal distribution.
        low (float): The lower bound of the truncated normal distribution.
        high (float): The upper bound of the truncated normal distribution.

    Methods:
        None
    """
    def __init__(self, mu: float, sigma: float, low: float, high: float) -> None:
        self.mu = mu
        self.sigma = sigma
        self.low = low
        self.high = high

    def sample(self, shape: tuple, column_wise_sampling: bool) -> np.ndarray:
        """
        Generate an array of sampled values from a truncated normal distribution.

        Args:
            shape (tuple): The shape of the output array to be generated.
            column_wise_sampling (bool): If True, samples values column-wise; otherwise, samples randomly
                                         accross rows and columns.

        Returns:
            np.ndarray: An array of sampled values from the truncated normal distribution.
        """
        sample_function = (
            bd.truncated_normal_1d
            if column_wise_sampling
            else bd.truncated_normal_2d)
        _: np.ndarray = sample_function(
            shape=shape,
            mu=self.mu,
            sigma=self.sigma,
            low=self.low,
            high=self.high)
        return _


class Triangular(Distribution):
    def __init__(self, low: float, high: float, mode: float) -> None:
        self.low = low
        self.high = high
        self.mode = mode

    def sample(self, shape: tuple, column_wise_sampling: bool) -> np.ndarray:
        sample_function = (bd.triangular_1d
                           if column_wise_sampling
                           else bd.triangular_2d)
        _: np.ndarray = sample_function(shape=shape, low=self.low, high=self.high, mode=self.mode)
        return _
