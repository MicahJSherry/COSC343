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
        F[7] = w1*x1**7 + w2*x2**7 + w3*x3**7 + w4*x4**7

        return F

    def Jacobian(X):
        
        w1 = X[0]
        w2 = X[1]
        w3 = X[2]
        w4 = X[3]
        x1 = X[4]
        x2 = X[5]
        x3 = X[6]
        x4 = X[7]

        J = np.zeros(8*8).reshape(8,8)
        
        #the compoenents come from the partial derivatives
        # (row col),(i,j) compenetnt is d f_i(x)/ d x_j
        
        #  partial derivitives of f_0 with respect to w_i
        J[0,0] = 1
        J[0,1] = 1
        J[0,2] = 1
        J[0,3] = 1
        #  partial derivitives of f_0 with respect to x_i
        J[0,4] = 0
        J[0,5] = 0
        J[0,6] = 0
        J[0,7] = 0

        #  partial derivitives of f_1 with respect to w_i
        J[1,0] = x1
        J[1,1] = x2
        J[1,2] = x3
        J[1,3] = x4
        #  partial derivitives of f_1 with respect to x_i
        J[1,4] = w1
        J[1,5] = w2
        J[1,6] = w3
        J[1,7] = w4

        #  partial derivitives of f_2 with respect to w_i
        J[2,0] = x1**2
        J[2,1] = x2**2
        J[2,2] = x3**2
        J[2,3] = x4**2
        #  partial derivitives of f_2 with respect to x_i
        J[2,4] = 2*w1*x1
        J[2,5] = 2*w2*x2
        J[2,6] = 2*w2*x2
        J[2,7] = 2*w2*x2
           

        #  partial derivitives of f_3 with respect to w_i
        J[3,0] = x1**3
        J[3,1] = x2**3
        J[3,2] = x3**3
        J[3,3] = x4**3
        #  partial derivitives of f_3 with respect to x_i
        J[3,4] = 3*w1*x1**2
        J[3,5] = 3*w2*x2**2
        J[3,6] = 3*w2*x2**2
        J[3,7] = 3*w2*x2**2

        #  partial derivitives of f_4 with respect to w_i
        J[4,0] = x1**4
        J[4,1] = x2**4
        J[4,2] = x3**4
        J[4,3] = x4**4
        # 4partial derivitives of f_4 with respect to x_i
        J[4,4] = 4*w1*x1**3
        J[4,5] = 4*w2*x2**3
        J[4,6] = 4*w2*x2**3
        J[4,7] = 4*w2*x2**3
           
        
        #  partial derivitives of f_5 with respect to w_i
        J[5,0] = x1**5
        J[5,1] = x2**5
        J[5,2] = x3**5
        J[5,3] = x4**5
        # partial derivitives of f_5 with respect to x_i
        J[5,4] = 5*w1*x1**4
        J[5,5] = 5*w2*x2**4
        J[5,6] = 5*w2*x2**4
        J[5,7] = 5*w2*x2**4
        
        #  partial derivitives of f_6 with respect to w_i
        J[6,0] = x1**6
        J[6,1] = x2**6
        J[6,2] = x3**6
        J[6,3] = x4**6
        # partial derivitives of f_6 with respect to x_i
        J[6,4] = 6*w1*x1**5
        J[6,5] = 6*w2*x2**5
        J[6,6] = 6*w2*x2**5
        J[6,7] = 6*w2*x2**5
        
        #  partial derivitives of f_7 with respect to w_i
        J[7,0] = x1**7
        J[7,1] = x2**7
        J[7,2] = x3**7
        J[7,3] = x4**7
        # partial derivitives of f_7 with respect to x_i
        J[7,4] = 7*w1*x1**6
        J[7,5] = 7*w2*x2**6
        J[7,6] = 7*w2*x2**6
        J[7,7] = 7*w2*x2**6
        return J


    def vectorNewtonsMethod(X,Jacobian=Jacobian, f=f, tol = 1e-7, maxIter=1000):
        s = np.ones(8).reshape(8,1)
        i = 0
        while(np.linalg.norm(s)>tol) and  i < maxIter:
            js = Jacobian(X)
            b  = -f(X)
            s = np.linalg.solve(js,b)
            print("X=",X,"i=",i)
            X += s
            i +=1
        return(X)
    return vectorNewtonsMethod( 10*np.random.rand(8,1))

#print(get_weights())


from sympy import symbols, Eq, solve

w1, w2, w3, w4, x1, x2, x3, x4 = symbols('w1 w2 w3 w4 x1 x2 x3 x4')

eq1 = Eq(w1 + w2 + w3 + w4, 2)
eq2 = Eq(w1*x1 + w2*x2 + w3*x3 + w4*x4, 0)
eq3 = Eq(w1*x1**2 + w2*x2**2 + w3*x3**2 + w4*x4**2, 2/3)
eq4 = Eq(w1*x1**3 + w2*x2**3 + w3*x3**3 + w4*x4**3, 0)
eq5 = Eq(w1*x1**4 + w2*x2**4 + w3*x3**4 + w4*x4**4, 2/5)
eq6 = Eq(w1*x1**5 + w2*x2**5 + w3*x3**5 + w4*x4**5, 0)
eq7 = Eq(w1*x1**6 + w2*x2**6 + w3*x3**6 + w4*x4**6, 2/7)
eq8 = Eq(w1*x1**7 + w2*x2**7 + w3*x3**7 + w4*x4**7, 0)

solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8), (w1, w2, w3, w4,x1,x2,x3,x4))
print(solution)