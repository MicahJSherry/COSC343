
import numpy as np
import matplotlib.pyplot as plt
def approximate_gamma():
    s = 0
    i = 0 
    nVec = []
    gammaVec = []
    for n in range(1,5000):
        step = 1.0/n 
        s += step 
        gamma = s - np.log(n)
        if (n)% 100 == 0:
            nVec.append(n)
            gammaVec.append(gamma)
    plt.plot(nVec,gammaVec)
    plt.ylabel("gamma")
    plt.xlabel("n")

    plt.show()


def f(x):
    return np.tan(x)
def finite_difference(x,h):
    return (f(x + h) - f(x))/h

def finite_difference2(x,h):
    return (f(x + h) - f(x-h))/(2*h)

def plot_error_finite_diffrence():
    x = 1
    k = 17
    true = (1/np.cos(x))**2

    errVec = []
    hVec= []


    print("The value we want is: ", true)

    for i in range (k):
        # The value of h gets smaller in this loop.
        h = 10**-i
        ans = finite_difference(x,h)

        AbsError = np.abs(true - ans)
        errVec.append(AbsError)
        hVec.append(h)
        
        #print("h =", h)
        #print("AbsError = ", AbsError)
        
        #print("iteration :", i )
    print(np.min(errVec))
    plt.loglog(hVec, errVec, 'k') 
    plt.show()



def plot_error_finite_diffrence2():
    x = 1
    k = 17
    true = (1/np.cos(x))**2

    errVec = []
    hVec= []


    print("The value we want is: ", true)

    for i in range (k):
        # The value of h gets smaller in this loop.
        h = 10**-i
        ans = finite_difference2(x,h)

        AbsError = np.abs(true - ans)
        errVec.append(AbsError)
        hVec.append(h)
        
        #print("h =", h)
        #print("AbsError = ", AbsError)
        
        #print("iteration :", i )
    print(np.min(errVec))
    plt.loglog(hVec, errVec, 'k') 
    plt.show()
plot_error_finite_diffrence()