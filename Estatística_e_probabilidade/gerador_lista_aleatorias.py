import numpy as np

def gera_lista_inteiros_aleatoria (num_linhas, num_colunas, min=0, max=10):
    lista = []
    for i in range(num_linhas):
        lista.append(np.random.randint(max-min, size=(num_colunas)))
        for n in range(num_colunas-1):
            lista[-1][n] += min
    return lista

def gera_lista_float_aleatoria (num_linhas, num_colunas, min=0, max=10, casas=2):
    lista = []
    max = (max-min)*(10**casas)

    for i in range(num_linhas):
        x = []
        for i in range(num_colunas):
            x.append(np.random.randint(max)*1.0)
            #print(x)
        lista.append(x)
        #print(lista)
        for n in range(num_colunas):
            #print(lista[-1][n])
            lista[-1][n] /= (10**casas)*1.00
            lista[-1][n] += min
    return lista