import numpy as np


def linear_regression_fit(x, y):
    n = len(x)

    # Calculate mean of x and y
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate the deviations from the mean
    x_deviations = x - x_mean
    y_deviations = y - y_mean

    # Calculate the covariance and variance of x and y
    covariance = np.cov([x_deviations, y_deviations])[0, 1]
    variance_x = np.var(x_deviations)

    # Calculate the coefficients
    m = covariance / variance_x
    b = y_mean - m * x_mean

    return m, b


# run
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

m, b = linear_regression_fit(x, y)
print(f'Coefficients: m = {m}, b = {b}')
