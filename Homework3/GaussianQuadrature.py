import numpy as np
import matplotlib.pyplot as plt

def fourPointGaussianQuad(f):
    """ 
    the points and weighs in this method come from solving the system :
    w1*x1^0 + w2*x2^0 + w3*x3^0 + w4*x4^0 = 2
    w1*x1^1 + w2*x2^1 + w3*x3^1 + w4*x4^1 = 0
    w1*x1^2 + w2*x2^2 + w3*x3^2 + w4*x4^2 = 2/3
    w1*x1^3 + w2*x2^3 + w3*x3^3 + w4*x4^3 = 0
    w1*x1^4 + w2*x2^4 + w3*x3^4 + w4*x4^4 = 2/5
    w1*x1^5 + w2*x2^5 + w3*x3^5 + w4*x4^5 = 0
    w1*x1^6 + w2*x2^6 + w3*x3^6 + w4*x4^6 = 2/7 
    w1*x1^7 + w2*x2^7 + w3*x3^7 + w4*x4^7 = 0
    """
    w = [0.347854845137454,   0.652145154862546, 
         0.652145154862546, 0.347854845137454]
   
    x = [-0.861136311594053, -0.339981043584856, 
         0.339981043584856, 0.861136311594053]
    area = 0
    for i in range(len(w)):
        area += w[i]*f(x[i])
    return area

def GaussianQuadrature(f,a,b): 
    #this method workes by linearly mapping [a,b] to [-1,1] and multiplying by (b-a)/2
    w = [0.347854845137454,   0.652145154862546, 
         0.652145154862546, 0.347854845137454]
   
    x = [-0.861136311594053, -0.339981043584856, 
         0.339981043584856, 0.861136311594053]
    slope = (b-a)/2 
    def map(x):
        # derived from the point-slope form of a line
        return slope * (x+1) + a
    area = 0
    for i in range(len(w)):
        area += slope*w[i] * f(map(x[i]))
    return area


def compositeQuadrature(f,A,B,intSize=1):
    intSize = intSize if intSize <= (A-B)/2 else 1
    NumInt = int((B-A)/intSize) 
    print(NumInt)
    x_points= np.linspace(A,B,NumInt)
    area = 0
    for i in range(len(x_points)-1):
        area += GaussianQuadrature(f,x_points[i],x_points[i+1])
    return area
     