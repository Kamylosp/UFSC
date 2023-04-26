from lista_5 import *
import numpy as np
import matplotlib.pyplot as plt


def l(n):
    if (n==1):
        return 0
    return n*l(n-1) + 3*(n-1) + 2


t = 1220298277
n_operacoes = t* 1.0e8

print(lista_5_ex_6_esc(t))
