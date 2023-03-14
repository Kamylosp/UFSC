from graficos import boxplot as bx
import operacoes as op
import numpy as np

#lista = np.random.normal((3, 5, 4, 5, 6), (1.25, 1.00, 1.25, 1.8, 2.25), (3, 5))

lista = [[1.5, 2, 5, 9, 5], [3,4, 7, 1, 6], [5, 6, 2, 5, 4]]

lista2 = []
for i in range(5):
    lista2.append(np.random.randint(8, size=10))

op.printa_informacoes(lista[0])


grafico = bx(lista2)
grafico.mostrar_grafico()