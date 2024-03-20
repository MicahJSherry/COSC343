import numpy as np 
import matplotlib.pyplot as plt

def f(x):
    return (x-3)* np.exp(x)

def secant(x0, x1, f=f):
    return (f(x1) - f(x0)) / (x1-x0)


def secantMethod(x0, x1, f=f,trueroot=None, errorVec = [], tol=1e-7, N=100):
    size = np.abs(x1 - x0)
    if size <= tol:
        return x1 if trueroot is None else (x1, errorVec)
    if N <= 0:
        print(trueroot)
        return x1 if trueroot is None else (x1, errorVec)
    
    x2 = x0 - f(x0)/secant(x0, x1, f=f)
    
    if trueroot is not None:
        errorVec.append(np.abs(trueroot-x0))
        return secantMethod(x1, x2, f,trueroot, errorVec, tol, N=N-1)
    else:
        print("hellow")
        return secantMethod(x1, x2, f, None, errorVec, tol, N=N-1)

def findAlpha(vec):
    alphaVec = []
    for i in range(len(vec) - 3):
        a = np.log(vec[i+2] / vec[i+1])/ np.log(vec[i+1] / vec[i])
        alphaVec.append(a)
    return alphaVec


if __name__=="__main__":
    x, errorVec = secantMethod(10,9,trueroot=3)
    alphaVec = findAlpha(errorVec)
    plt.plot(alphaVec)
    plt.show()
    