import numpy as np
import matplotlib


def one_norm(matrix):
    max = 0
    for j in range(len(matrix[0])):
        sum = 0
        for i in range(len(matrix)):
            sum += np.abs(matrix[i][j])
        if sum > max:
            max = sum
    return max