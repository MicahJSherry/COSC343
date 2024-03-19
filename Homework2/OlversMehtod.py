import numpy as np 
import matplotlib.pyplot as plt


def f(x):
    return 
def fp(x):
    return
def fdp(x):
    return 



def olversMethod(x0,trueroot=None, f=f,fp=fp, fdp=fdp, tol=1e-7,N=100):
    size = 1.0
    errorVec = []
    i = 0
    while (size > tol and i < N):
        #print(size)
        x1   = x0 - (f(x0) / fp(x0)) - ((1/2) * (fdp(x0) / fp(x0)) * ((f(x0) / fp(x0)) ** 2))
        print(i, x1)
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
    x, errorVec = olversMethod(23, 0 ,f=f ,fp=fp,fdp=fdp)
    alphaVec = findAlpha(errorVec)
    print(alphaVec)
    plt.plot(alphaVec)
    plt.show()