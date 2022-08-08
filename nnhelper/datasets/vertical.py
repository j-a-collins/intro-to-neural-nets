import numpy as np


# Source: https://cs231n.github.io/neural-networks-case-study/
def create_data(samples, classes):
    x = np.zeros((samples * classes, 2))
    y = np.zeros(samples * classes, dtype="uint8")
    for class_number in range(classes):
        ix = range(samples * class_number, samples * (class_number + 1))
        x[ix] = np.c_[
            np.random.randn(samples) * 0.1 + class_number / 3,
            np.random.randn(samples) * 0.1 + 0.5,
        ]
        y[ix] = class_number
    return x, y
