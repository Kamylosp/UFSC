from lista_5 import *
import numpy as np


def f(h):
    return 20*np.arccos(1-h/2) + (5*h-10)*np.sqrt((4-h)*h) - 8

def f_(h):
    return 10 * np.sqrt((4-h)*h)

# print(newton(f, f_, 0.5))

# print(np.power(2, 3))





# Questão 5
# print( calculadora_do_cidadao (juros =0.021 , tempo =12 , prestacao =2854.23))

# print(calculadora_do_cidadao ( valor =30000 , tempo =12 , prestacao =2854.23))
# print("0.02099970")

# print(calculadora_do_cidadao ( valor =30000 , juros =0.021 , prestacao =2854.23))
# print("12.0")

# print(calculadora_do_cidadao ( valor =30000 , juros =0.021 , tempo =12))
# print("2854.23")