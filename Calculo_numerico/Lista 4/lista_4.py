# from lista_4_modulo import funcao_escondida
from prints import e_par
import numpy as np

# Questão 1
# def escondida_par(x):
#     if (funcao_escondida(x) % 2 == 0):
#         return True
#     return False

# Questão 2
def norma_op(A):
    matriz = np.array(A)

    matriz_transposta = matriz.transpose()
    
    produto_das_matrizes = np.matmul(matriz_transposta, matriz)

    matriz_de_autovalores, _ = np.linalg.eig(produto_das_matrizes)

    return np.sqrt(np.amax(matriz_de_autovalores))





def apaga_par (L):
    i = 0
    while i < len(L):
        if e_par (L[i]):
            L= L [:i] + L[i +1:]
        else:
            i+=1
    return L

T = [[1,2,3], [4,5,6]]
print(norma_op(T))