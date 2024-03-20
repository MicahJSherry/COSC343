import numpy as np 
import matplotlib.pyplot as plt


def f(x):
    return (((x - 3) ** 2) * (1 + np.exp(x)))      

def fp(x):
    return (x-3) * ((x - 1) * np.exp(x) + 2)


def multiplicy2_NewtonsMethod(x0,trueroot=None, f=f,fp=fp, tol=1e-7,N=100):
    size = 1.0
    errorVec = []
    i = 0
    while (size > tol and i < N) and f(x0) != 0:
        
        x1   = x0 - 2 * (f(x0) / fp(x0))
       
        if trueroot is not None:
            errorVec.append(np.abs(x1 - trueroot))
        
        size = np.abs(x1 - x0)
        x0   = x1
        i   += 1 
    
    if trueroot is not None:
        return x1, errorVec
    else:
        return x1
    
def NewtonsMethod(x0,trueroot=None, f=f,fp=fp, tol=1e-7,N=100):
    size = 1.0
    errorVec = []
    i = 0
    while (size > tol and i < N) and f(x0) != 0:
        
        x1   = x0 - (f(x0) / fp(x0))
        
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
    x1, errorVec1 = NewtonsMethod(4, 3 ,f=f ,fp=fp)
    x2, errorVec2 = multiplicy2_NewtonsMethod(4, 3 ,f=f ,fp=fp)
    
    alphaVec1 = findAlpha(errorVec1)
    alphaVec2 = findAlpha(errorVec2)
    print("newtons method approximation:",x1)
    print("accelerated newtons method approximation:",x2)

    plt.plot(alphaVec1)
    plt.show()
    plt.plot(alphaVec2)
    plt.show()