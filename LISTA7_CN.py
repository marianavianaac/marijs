import numpy as np
funcao= 12/5*x*(220-x)**2
fl= 160

def malha(func, a, b, n):
    x= np.linspace(a, b, n+1, dtype= float)
    y= func(x)
    h= (b-a)/n
    return y, h
def integral_trapezio(func,a, b, n):
    y,h= malha(func, a, b, n)
    S= y[0] + 2. * np.sum(y[1:-1]) + y[-1]
    return .5 * h * S
def  f(x):
    return np.funcao
print(integral_trapezio(f, 0, np.fl, 80))
