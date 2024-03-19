import numpy as np 
import matplotlib.pyplot as plt

def f(x):
    return (x-3)* np.exp(x)

def secant(x0, x1, f=f):
    return (f(x1) - f(x0)) / (x1-x0)

def secantNewtonsMethod(x0,x1,trueroot=None,f=f, tol=1e-7, N=100):
    size = 1.0
    errorVec = []
    i = 0
    while size > tol and i < N:
        print(i)
        print(x0)
        x2 = x0 - f(x0)/secant(x0, x1, f=f)
        if trueroot is not None:
            errorVec.append(np.abs(trueroot-x1))

        size = np.abs(x1 - x0)
        
        x0 = x1
        x1 = x2
        i += 1 
        
    if trueroot is None:
        return x2
    else:
        return x2, errorVec

def findAlpha(vec):
    alphaVec = []
    for i in range(len(vec) - 3):
        a = np.log(vec[i+2] / vec[i+1])/ np.log(vec[i+1] / vec[i])
        alphaVec.append(a)
    return alphaVec


if __name__=="__main__":
    x, errorVec = secantNewtonsMethod(10,9, trueroot=3 ,f=f )
    alphaVec = findAlpha(errorVec)
    print(alphaVec)
    plt.plot(alphaVec)
    plt.show()
    