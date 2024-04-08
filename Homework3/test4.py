from GaussianQuadrature import GaussianQuadrature

def f1(x):
    return 3.0

def f2(x):
    return -2.5*x + f1(x)

def f3(x, f2=f2):
    return 4.6*(x**2.0) + f2(x)

def f4(x, f3=f3):
    return -5.1*(x**3.0) + f3(x)
print(GaussianQuadrature(f4,0,1))
print(GaussianQuadrature(f4,-1,0))
