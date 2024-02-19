import numpy as np
import matplotlib.pyplot as plt


xvec = np.linspace(0.9, 1.1)
yvec = np.tan(xvec)

x = 1
h = 1/10

true_slope = (1/np.cos(x))**2

xline1 = [x, x + h]
xline2 = [x - h, x + h]
xy1 = (x - h, np.tan(x-h) )
xy2 = (x, np.tan(x))
xy3 = (x + h, np.tan(x+h) )

#plt.plot(xvec, yvec, "b")
plt.axline((1, np.tan(x)), slope =true_slope, color = "r" )
plt.axline(xy1=xy2, xy2=xy3, color = "g")
plt.axline(xy1=xy1, xy2=xy3, color = "k")
plt.show()