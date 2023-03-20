from graficos import boxplot as bx
import gerador_lista_aleatorias as aleatoria
import operacoes as op
import numpy as np


def printa_lista(lista):
    for i in lista:
        print(i)


lista_R = [[174.4,177.9,185.6,180.8,173.9,176.8,165.0,176.4,172.1,170.3,
       172.0,170.4,170.8,175.1,167.3,166.9,165.8,176.1,171.1,174.3,
       179.7,180.8,179.9,169.8,175.6,169.0,173.3,174.6,177.4,174.7,
       168.5,174.1,172.4,178.7,179.0,175.5,181.5,171.0,159.0,164.9,
       179.0,173.9,177.6,172.1,175.5,164.4,167.7,185.2,166.2,172.1]]

# TESTAR SE A GERA LISTA ALEATORIA FUNCIONA CORRETAMENTE
# lista3 = aleatoria.geran_lista_float_aleatoria(2, 3, casas=3)

# printa_lista(lista3)

# op.printa_informacoes(lista_R)

grafico = bx(lista_R)
# grafico.nome_das_barras(["Ind1", "Ind2", "Ind3", "Ind4", "Ind5"])
grafico.mostrar_grafico()