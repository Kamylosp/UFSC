from graficos import boxplot as bx
import operacoes as op
import numpy as np

def printa_matriz (matriz):
    for linha in matriz:
        op.printa_informacoes(linha)

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

    for i in range(num_linhas+1):
        lista.append(np.random.randint(max, size=(num_colunas)))
        #print(lista[-1])
        for n in range(num_colunas):
            print(lista[-1][n])
            lista[-1][n] /= (10**casas)
            lista[-1][n] += min
    
    return lista
            


lista = [[1.5, 2, 5, 9, 5], [3,4, 7, 1, 6], [5, 6, 2, 5, 4]]



# TESTAR SE A GERA LISTA ALEATORIA FUNCIONA CORRETAMENTE
lista3 = gera_lista_inteiros_aleatoria(3, 3)

print(lista3)

# lista2 = []
# for i in range(5):
#     lista2.append(np.random.randint(8, size=10))

op.printa_informacoes(lista3[0])

grafico = bx(lista3)
grafico.mostrar_grafico()