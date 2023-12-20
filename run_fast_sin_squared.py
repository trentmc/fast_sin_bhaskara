import numpy as np
FIVE_PI_SQUARED = 5 * np.pi ** 2
TWO_PI = 2 * np.pi

def fast_sin(x):
    """Returns an approximation of sin(x). x is in radians. Uses Bhaskara I."""
    if 0 <= x <= np.pi:
        return 16 * x * (np.pi - x) / (FIVE_PI_SQUARED - 4 * x * (np.pi - x))
    if np.pi < x <= TWO_PI:
        return -fast_sin(x - np.pi)
    if x < 0:
        return -fast_sin(-x)
    return fast_sin(unwrap_angle(x))

def unwrap_angle(x):
    """Converts any angle x in [2*pi, inf) to value in [0, 2*pi]. x in radians."""
    assert x > TWO_PI
    n_phases = x // TWO_PI
    return x - n_phases * TWO_PI

def fast_sin_squared(x):
    """Returns an approximation of sin(x) ** 2. x is in radians."""
    sin_x = fast_sin(x)
    return sin_x * sin_x # a * a is faster than a ** 2 in python

# def forward(self, x, s):
#   inv_a1, inv_a2 = 1/a1, 1/a2
#   for [all these vars]:
#     xt = n1(x, s)
#     xt.add_(inv_a1 * fast_sin_squared(a1 * xt))
#     xt = c1(xt)
#     xt = n2(xt, s)
#     xt.add_(inv_a2 * fast_sin_squared(a2 * xt))
#     xt = c2(xt)
#     x.add_(xt)
# return x

def plot_fast_sin():
    import matplotlib.pyplot as plt

    x = np.arange(-4.0, +4.0, 0.01) * np.pi
    sin_x = np.sin(x)
    sin_squared_x = np.sin(x) ** 2
    fast_sin_x = np.array([fast_sin(xi) for xi in x])
    fast_sin_squared_x = np.array([fast_sin_squared(xi) for xi in x])

    plt.plot(x, sin_x, "c-", label="sin(x)")
    plt.plot(x, fast_sin_x, "b--", label="fast_sin(x)")
    plt.plot(x, sin_squared_x, "y-", label="sin(x)^2")
    plt.plot(x, fast_sin_squared_x, "r--", label="fast_sin_squared(x)")
    plt.legend(loc="upper right")
    plt.xlabel("x, in radians")
    plt.ylim(-1.05, 1.6)
    plt.show()

plot_fast_sin()
