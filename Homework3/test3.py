import numpy as np
import matplotlib.pyplot as plt 
from GaussianQuadrature import fourPointGaussianQuad, GaussianQuadrature, compositeQuadrature, findAlpha

def f(x):
    return np.exp(x)*x**2

def F(x):
    return np.exp(x)*(x**2-2*x+2)

if  __name__=="__main__":
    a = -10
    b = 2
    true_val = F(b)-F(a)
    print(true_val)
    print(compositeQuadrature(f, a, b))
    errorVec = []
    for i in range(10):
        approx =compositeQuadrature(f, a, b, numInt=2**i)
        print(approx)
        errorVec.append(np.abs(true_val-approx))

    alpha = findAlpha(errorVec)
    #print(alpha)
    plt.plot(alpha)
    plt.show()