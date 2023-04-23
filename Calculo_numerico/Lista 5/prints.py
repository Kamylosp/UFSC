from lista_5 import *
import numpy as np


def f(h):
    return 20*np.arccos(1-h/2) + (5*h-10)*np.sqrt((4-h)*h) - 8

def f_(h):
    return 10 * np.sqrt((4-h)*h)

print(newton(f, f_, 0.5))

print(np.power(2, 3))
