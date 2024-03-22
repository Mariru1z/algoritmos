#crear un códifo que resuelva 2x^3+x^2 =1 por newton raphson en python
#como algoritmo matematico  2x^3+x^2 =1 con metodo de newton raphson?
def func(x):
    return 2*x**3 + x**2 - 1

def derivada(x):
    return 6*x**2 + 2*x

