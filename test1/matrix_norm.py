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
        
def inf_norm(matrix):
    max = 0
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[0])):
            sum += np.abs(matrix[i][j])
        if sum > max:
            max = sum
    return max
           


matrix = [[1,2,0],
          [1,0,0],
          [1,0,0],
          [1,0,0]]
#matrix = np.zeros(9).reshape(3,3)

print(inf_norm(matrix))