import numpy as np


w_0 = 10
epsilon = 0.02


def function(t, y):

    y_1 = y[0]
    y_2 = y[1]
    y_1_derived = y_2
    y_2_derived = -2 * epsilon * w_0 * y

    return y_1_derived, y_2_derived


def euler_method(t_n, y_n, h):

    return y_n + h * function(t_n, y_n)


def heun_method(t_n, y_n, h):

    return y_n + (h / 2) * (
        function(t_n, y_n) + function(t_n + h, y_n + h * function(t_n, y_n))
    )


def midpoint_method(t_n, y_n, h):

    return y_n + h * function(t_n + h / 2, y_n + (h / 2) * function(t_n, y_n))
