from lista_5 import *
import numpy as np
import matplotlib.pyplot as plt

# def f(h):
#     return 20*np.arccos(1-h/2) + (5*h-10)*np.sqrt((4-h)*h) - 8

# def f_(h):
#     return 10 * np.sqrt((4-h)*h)

t_critica, p_critica = 190.6, 4599
massa_esperada = 1069.0033540184766

a = (0.427 * (R*R) * np.power(t_critica, 2.5)) / (p_critica)
b = (0.0866 * R * t_critica) / (p_critica)

# print(Q4_f(3/massa_esperada, a, b))


# print(lista_5_ex_4(t_critica,p_critica))

# def fat(x):
#     out = 1
#     while (x > 1):
#         out *= x
#         x -= 1
#     return out



# e = np.exp(1)

# def l2(n):
#     return 2*(1+e)*fat(n)

# delta = []
# for i in range(1, 100):
#     print((l2(i)/1.12822061206908 - l(i))/l(i))

print(l(673217))