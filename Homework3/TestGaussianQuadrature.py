import numpy as np
import matplotlib.pyplot as plt 
from GaussianQuadrature import fourPointGaussianQuad, GaussianQuadrature

def f1(x):
    return (2*x**7 - 3*x**6 + 5*x**5 - 
            4*x**4 + x**3 - 2*x**2 + 3*x - 1)

def F1(x):
    # antiderivative of f1(x)
    return  (2/8*x**8 - 3/7*x**7 + 5/6*x**6 - 4/5*x**5 +
             1/4*x**4 - 2/3*x**3 + 3/2*x**2 - x)
def f2(x):
    return x**6

def F2(x):
    # antiderivative of f2(x)
    return  x**7/7

if   __name__=="__main__":
    trueVal_f1 =  F1(10) - F1(-10) 
    print(trueVal_f1)
    print(fourPointGaussianQuad(f1))
    print(GaussianQuadrature(f1,-10,10))
    print()
    trueVal_f2 =  F2(1) - F2(-1)
    print(trueVal_f2)
    print(fourPointGaussianQuad(f2))
    print(GaussianQuadrature(f2,-1,1))