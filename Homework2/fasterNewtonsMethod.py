import numpy as np 
import matplotlib.pyplot as plt


def f(x):
    return ((x - 3) ** 2) * np.exp(x)

def fp(x):
    return 2*(x - 3) * np.exp(x)+((x - 3) ** 2) * np.exp(x)


def NewtonsMethod(x0,trueroot=None, f=f,fp=fp, tol=1e-7,N=100):
    size = 1.0
    errorVec = []
    i = 0
    while (size > tol and i < N) or f(x0) != 0:
        print(size)
        x1   = x0 - 2 * (f(x0) / fp(x0))
        print(x1)
        if trueroot is not None:
            errorVec.append(np.abs(x1 - trueroot))
        
        size = np.abs(x1 - x0)
        x0   = x1
        i   += 1 
    
    if trueroot is not None:
        return x1, errorVec
    else:
        return x1

def findAlpha(vec):
    alphaVec = []
    for i in range(len(vec) - 3):
        a = np.log(vec[i+2] / vec[i+1]) / np.log(vec[i+1] / vec[i])
        alphaVec.append(a)
    return alphaVec


if __name__=="__main__":
    x, errorVec = NewtonsMethod(10, 3 ,f=f ,fp=fp)
    alphaVec = findAlpha(errorVec)
    print(alphaVec)
    plt.plot(alphaVec)
    plt.show()