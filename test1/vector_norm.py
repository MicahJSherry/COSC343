import numpy as np
import matplotlib


def p_norm(vec, p):
    sum = 0
    for element in vec:
        sum += np.abs(element) ** p
    return sum ** (1/p)


vec = [3,4] 
p = 2
pnorm = p_norm(vec,p)
print("the", p, "norm of", vec, "is ", pnorm) 
