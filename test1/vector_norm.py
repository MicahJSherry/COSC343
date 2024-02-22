import numpy as np
import matplotlib


def p_norm(vec, p):
    sum = 0
    for element in vec:
        sum += np.abs(element) ** p
    return sum ** (1/p)


