import numpy as np 
import matplotlib.pyplot as plt
from Runge_Kutta import simulate_model
from matplotlib.widgets import Slider


def Leslie_Gower_forcing_funtion(a1, a2, b1, b2):
    def f(t,Y):
        Ynew = np.zeros(2).reshape(2,1)
        Ynew[0] = (a1-b1*Y[1])*Y[0]
        Ynew[1] = Y[1]*(a2-b2*Y[1]/Y[0])

        return Ynew
    return f
f = Leslie_Gower_forcing_funtion(.5, 1, .1, 10)
prey = 100
pred = 10
tvec,uvec,vvec =simulate_model(f,prey_inital=prey, predator_inital=pred)
print(vvec)

print(uvec)
plt.plot(tvec,uvec, "k")
plt.plot(tvec,vvec, "g")
plt.title("Leslie-Gower with inital Conditions y1 = "+ str(prey)+" and y2 = " + str(pred) )
plt.show()

plt.plot(uvec,vvec)
plt.title("Leslie-Gower phase portrait with inital Conditions y1 = "+ str(prey)+" and y2 = " + str(pred) )
plt.show()



