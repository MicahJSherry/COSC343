import matplotlib.pyplot as plt
import numpy as np 
from numpy.random import rand 



def f(X):
    w1 = X[0]
    w2 = X[1]
    x1 = X[2]
    x2 = X[3]
    
    F = np.zeros(4).reshape(4,1)    

    F[0] = w1         + w2         - 2
    F[1] = w1*x1      + w2*x2      - 0
    F[2] = w1*x1 ** 2 + w2*x2 ** 2 - 2/3
    F[3] = w1*x1 ** 3 + w2*x2 ** 3 - 0
    
    return F

def Jacobian(X):
    
    w1 = X[0]
    w2 = X[1]
    x1 = X[2]
    x2 = X[3]

    J = np.zeros(4*4).reshape(4,4)
    
    #the compoenents come from the partial derivatives
    # (row col),(i,j) compenetnt is d f_i(x)/ d x_j
    
    #  partial derivitives of f_0
    J[0,0] = 1
    J[0,1] = 1
    J[0,2] = 0
    J[0,3] = 0

    #  partial derivitives of f_1
    J[1,0] = x1
    J[1,1] = x2
    J[1,2] = w1
    J[1,3] = w2

    #  partial derivitives of f_2
    J[2,0] = x1**2 
    J[2,1] = x2**2
    J[2,2] = 2*w1*x1 
    J[2,3] = 2*w2*x2
    
    #  partial derivitives of f_3
    J[3,0] = x1**3
    J[3,1] = x2**3
    J[3,2] = 3*w1*x1**2 
    J[3,3] = 3*w2*x2**2 

    return J


def vectorNewtonsMethod(X,Jacobian=Jacobian, f=f, tol = 1e-7, maxIter=1000):
    s = np.ones(4).reshape(4,1)
    i = 0
    while(np.linalg.norm(s)>tol) and  i < maxIter:
        js = Jacobian(X)
        b  = -f(X)
        #print(js)
        #print(b)
        s = np.linalg.solve(js,b)
        X += s
        i +=1
    return(X)


if __name__=="__main__":
    X = -10 + 5*rand(4,1)

    X = vectorNewtonsMethod(X)
    print(X)
    print(f(X))

