from graficos import boxplot as bx
import gerador_lista_aleatorias as aleatoria
import operacoes as op
import numpy as np

def printa_lista(lista):
    for i in lista:
        print(i)

# TESTAR SE A GERA LISTA ALEATORIA FUNCIONA CORRETAMENTE
lista3 = aleatoria.gera_lista_float_aleatoria(2, 3, casas=3)

printa_lista(lista3)

# op.printa_informacoes(lista3[0])

grafico = bx(lista3)
grafico.titulo("Elisson é foda", 10)
# grafico.nome_das_barras(["Ind1", "Ind2", "Ind3", "Ind4", "Ind5"])
grafico.mostrar_grafico()