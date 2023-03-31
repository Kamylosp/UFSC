# from lista_4_modulo import funcao_escondida
from prints import e_par

# Questão 1
# def escondida_par(x):
#     if (funcao_escondida(x) % 2 == 0):
#         return True
#     return False

def apaga_par (L):
    i =0
    while i < len( L):
        if e_par (L[i]) :
            L= L [:i] + L[i +1:]
        else:
            i+= 1
    return L

L = [1, 5, 4, 7, 1, 2, 3]
print(L)