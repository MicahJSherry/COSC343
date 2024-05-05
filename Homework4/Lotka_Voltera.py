import numpy as np 
import matplotlib.pyplot as plt
from Runge_Kutta import simulate_model



def Lotka_Voltera_forcing_funtion(a1, a2, b1, b2):
    def f(t,Y):
        Ynew = np.zeros(2).reshape(2,1)
        Ynew[0] = (a1-b1*Y[1])*Y[0]
        Ynew[1] = (-a2+b2*Y[0])*Y[1]

        return Ynew
    return f

# initalize the model with the give parameters 
f = Lotka_Voltera_forcing_funtion(.5, 1, .1, .02)


prey = 100
pred = 10 
tvec,uvec,vvec =simulate_model(f,prey_inital=prey, predator_inital=pred)
plt.plot(tvec,uvec, "k")
plt.plot(tvec,vvec, "g")
plt.title("Lotka-Voltera with inital Conditions y1 = "+ str(prey)+" and y2 = " + str(pred) )
plt.show()

plt.plot(uvec,vvec)
plt.title("Lotka-Voltera phase portrait with inital Conditions y1 = "+ str(prey)+" and y2 = " + str(pred) )
plt.show()