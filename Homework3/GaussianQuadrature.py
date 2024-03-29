import numpy as np
import matplotlib.pyplot as plt

def get_weights():
    def f(X):
        w1 = X[0]
        w2 = X[1]
        w3 = X[2]
        w4 = X[3]
        x1 = X[4]
        x2 = X[5]
        x3 = X[6]
        x4 = X[7]

        F = np.zeros(8).reshape(8,1)    

        F[0] = w1       + w2       + w3       + w4       - 2
        F[1] = w1*x1    + w2*x2    + w3*x3    + w4*x4    
        F[2] = w1*x1**2 + w2*x2**2 + w3*x3**2 + w4*x4**2 - 2/3
        F[3] = w1*x1**3 + w2*x2**3 + w3*x3**3 + w4*x4**3 
        F[4] = w1*x1**4 + w2*x2**4 + w3*x3**4 + w4*x4**4 - 2/5
        F[5] = w1*x1**5 + w2*x2**5 + w3*x3**5 + w4*x4**5
        F[6] = w1*x1**6 + w2*x2**6 + w3*x3**6 + w4*x4**6 - 2/7 
        F[7] = w1*x1**7 + w2*x2**7 + w3*x3**7 + w4*x4**7 - 2/3

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
            s = np.linalg.solve(js,b)
            X += s
            i +=1
        return(X)





