import numpy as np
import matplotlib
from random import randint

from Latex_generator import *

def p_norm(vec, p):
    sum = 0
    for element in vec:    
        if not isinstance(element,(int,float)): # nonnumeric or wrong shape 
            raise TypeError("elments of the vector must be numbers") 
        
        sum += np.abs(element) ** p
    
    return sum ** (1/p)


if __name__ == "__main__":
    """testing and formating the p_norm function"""
    for i in range(4,7):
        vec = []
        for j in range(i):
            vec.append(randint(-10, 10))
        p = randint(1,3)
        ans  = round(p_norm(vec, p),3)
        latex = vector_to_latex(vec)
        print(pnorm_to_latex(latex ,p, ans))


