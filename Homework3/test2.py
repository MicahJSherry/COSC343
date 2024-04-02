import numpy as np
import matplotlib.pyplot as plt 
from GaussianQuadrature import fourPointGaussianQuad, GaussianQuadrature, compositeQuadrature

def f1(x):
    return (2*x**7 - 3*x**6 + 5*x**5 - 
            4*x**4 + x**3 - 2*x**2 + 3*x - 1)

def F1(x):
    # antiderivative of f1(x)
    return  (2/8*x**8 - 3/7*x**7 + 5/6*x**6 - 4/5*x**5 +
             1/4*x**4 - 2/3*x**3 + 3/2*x**2 - x)
def f3(x):
    return 12*x**7 + x**4 - 10 * x **2+ 42 * x 

def F3(x):
    # antiderivative of f3(x)
    return 12/8*x**8 + x**5/5 - 10/3 * x **3+ 21 * x**2
    

if   __name__=="__main__":
    trueVal_f1 =  F1(1) - F1(-1) 
    print(trueVal_f1)
    print(fourPointGaussianQuad(f1))
    print(GaussianQuadrature(f1,-1,1))
    
    a = -2
    b = 3
    trueVal_f2 =  F3(b) - F3(a)
    print(trueVal_f2)
    
    print(GaussianQuadrature(f3,a,b))
   