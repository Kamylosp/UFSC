import lista_3 as l
from decimal import Decimal
from math import pi, sin, cos

# Questão 1
x = 9.3132257e-10
y = Decimal(2.4)

# for i in range(1, 21):
#     if (abs(cos(pi/i) - l.cos(pi/i)) < x):
#         print(f"Passou no teste - pi/{i}")


# Questão 2


# Questão 3
L = [3, 2, 1]
A = l.reversa(L)
#print("L:          ", L)
l.reverter(L)
#print("reverter(L):", L)
#print("reversa(L): ", A)


# Questão 4
lista = [1, 5, 8, 1, 2, 6, 7, 0]
l.ordena(lista)
print(lista)



# Questão 5