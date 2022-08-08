import numpy as np


def create_data(samples=1000):
    """Creates a sine sample dataset"""
    x = np.arange(samples).reshape(-1, 1) / samples
    y = np.sin(2 * np.pi * x).reshape(-1, 1)

    return x, y
