from numpy import *

def f(x):
    return 4*cos(x) - exp(x)

def f_(x):
    return -4*sin(x)- exp(x)

def g(x):
    return x - exp(x-2)

def g_(x):
    return 1 - exp(x-2)

def h(x):
    return 2*x*x -5*x +2

def h_(x):
    return 4*x - 5

def i(x):
    return x*exp(-x) - exp(-3)

def i_(x):
    return exp(-x) - x*exp(-x)

def j(x):
    return -x*x*x*x + 3*x*x +2

def j_(x):
    return -4*x*x*x + 6*x

# x = float(input("Digite um numero: "))
tol = 10**(-3)
print(tol)

for n in range(-5, 5):
    print(f"j({n}) = {j(n)}")

x = 2

# Ponto médio = 1.25
cont = 0
print(f"{cont} : {x}")
while True:
    x2 = x - j(x)/j_(x)

    if (abs(x2-x)/abs(x2) < tol):
        print("Erro absoluto: ",abs(x2-x)/x2)
        break
    x = x2
    cont+= 1
    print(f"{cont} : {x}")
print("Resultado: ", x)