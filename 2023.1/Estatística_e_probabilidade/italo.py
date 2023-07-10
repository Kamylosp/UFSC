from graficos import boxplot as bx
import gerador_lista_aleatorias as aleatoria
import operacoes as op
import numpy as np
import matplotlib.pyplot as plt

def printa_lista(lista):
    for i in lista:
        print(i)


lista_R = [[172, 132, 166, 186, 243, 186, 209, 128, 169, 178,
            221, 191, 196, 169, 119, 119, 135, 78, 162, 186, 
            135, 149, 124, 114, 95, 136, 116, 103, 119, 114,
            176, 180, 186, 187, 199, 188, 157, 151, 164, 165]]

# TESTAR SE A GERA LISTA ALEATORIA FUNCIONA CORRETAMENTE
# lista3 = aleatoria.geran_lista_float_aleatoria(2, 3, casas=3)

# printa_lista(lista3)

# op.printa_informacoes(lista_R)

grafico = bx(lista_R)
# grafico.nome_das_barras(["Ind1", "Ind2", "Ind3", "Ind4", "Ind5"])

grafico.mostrar_grafico()


plt.hist(lista_R, 7, rwidth=0.9)
plt.show()