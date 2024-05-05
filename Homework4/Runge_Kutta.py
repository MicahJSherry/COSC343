import numpy as np 

def  simulate_model(f, prey_inital = 100, predator_inital = 10, t0=0, T=25, steps = 2000):
    """ a method to simmulate a preditor prey model for a given a forcing fuction """
    
    # set up model inital conditions 
    h = (T-t0)/steps # change in time step  
    Y = np.zeros(2).reshape(2,1)
    Y[0] = prey_inital
    Y[1] = predator_inital
    tvec = []
    preyVec = []
    predatorVec = []
    t=t0

    for i in range(steps):
        t = t + h
        Y = RungeKutta4(t,h,Y,f)
        prey = Y[0]
        preditor = Y[1] 
        
        tvec.append(i)
        preyVec.append(prey)
        predatorVec.append(preditor)
        #if prey <=0 or preditor <=0:
        #    print(prey, preditor)
        #    break
    return tvec, preyVec, predatorVec  

def RungeKutta4(t,h,Y,f):
    """a fourth order runge kuta method"""
    K1 = f(t,Y)
    K2 = f(t+.5*h, Y+.5*K1)
    K3 = f(t+.5*h, Y+.5*K2)
    K4 = f(t+h, Y+K3)
    
    return Y + (h/6)*(K1 + 2*K2 + 2*K3 + K4)