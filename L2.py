import math

xi=float(input('Digite o valor de x(0): '))
e= float(input('Digite o valor da precisão necessária: '))
xk= 999999.999
contador= 0

def teste(x):
    fx= -1.157407407*10**(-13) * x**4 + 5*10**(-8)*x**2 -3*10**-3
    fdx= (-1.157407407*10**(-13))* 4 * x**3 + (5*10**(-8))*2*x
    divisao= fx/fdx
    return divisao

while (abs((xk-xi)/xk)) > e or contador == 500:
    x= xi
    xi= (x) - teste(x)
    x= xi
    xk= (x) - teste(x)
    contador = contador + 1

print('O valor da raiz aproximada encontrada foi: {}'.format(xk))
print('O valor de interações feitas foi: {}'.format(contador))
