import numpy as np 
import matplotlib.pyplot as plt

def RungeKutta4(t,h,U,f):
   
    K1 = f(t,U)
    K2 = f(t+.5*h, U+.5*K1)
    K3 = f(t+.5*h, U+.5*K2)
    K4 = f(t+h, U+K3)
    
    return U + (h/6)*(K1 + 2*K2 + 2*K3 + K4)


def Leslie_Gower_forcing_funtion(a1, a2, b1, b2):
    def f(t,U):
        Unew = np.zeros(2).reshape(2,1)
        Unew[0] = (a1-b1*U[1])*U[0]
        Unew[1] = U[1]*(a2-b2*U[1]/U[0])

        return Unew
    return f
f = Leslie_Gower_forcing_funtion(.5, 1, .1, 5)

def  foo(t0=0, u0 = 25, v0 = 10, T=25, steps = 2000):
    h = (T-t0)/steps 
    #intitalizes the you
    U = np.zeros(2).reshape(2,1)
    U[0] = u0
    U[1] = v0
   
    
   
    tvec = []
    uvec = []
    vvec = []
    t=t0
    for i in range(steps):
        t = t + h
        U = RungeKutta4(t,h,U,f)
        u0 = U[0]
        v0 = U[1] 
        tvec.append(i)
        uvec.append(u0)
        vvec.append(v0)
    return tvec,uvec,vvec  
tvec, uvec, vvec = foo()     
plt.plot(tvec,uvec)
plt.plot(tvec,vvec)
plt.show()