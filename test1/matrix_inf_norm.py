import numpy as np
import matplotlib
from  random import randint

from Latex_generator import *

def inf_norm(matrix):
    max = 0
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        sum = 0
        if len(matrix[i]) != n: # wrong shape
            raise ValueError("Matrix must be rectangular")
            
        for j in range(n):
            element = matrix[i][j]
            if not isinstance(element,(int,float)): # nonnumeric or wrong shape 
                raise TypeError("elments of the vector must be numbers") 
            sum += np.abs(element)

        if sum > max:
            max = sum
    return max

if __name__=="__main__":
    """ test inf_norm  """
    
    for i in range(3):
        m = randint(3,5)
        n = randint(3,5)
        matrix = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(randint(-10,10))
            matrix.append(row)
        p = "\\infty"
        ans = inf_norm(matrix)
        matrix_latex = matrix_to_latex(matrix)
        print(pnorm_to_latex(matrix_latex, p, ans))
