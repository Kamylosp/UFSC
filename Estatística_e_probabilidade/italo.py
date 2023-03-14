from graficos import boxplot as bx
import numpy as np

np.random.seed(10)
#lista = np.random.normal((3, 5, 4, 5, 6), (1.25, 1.00, 1.25, 1.8, 2.25), (3, 5))
#lista = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (3, 3))

lista = [[1.5, 2, 5, 9, 5], [3,4, 7, 1, 6], [5, 6, 2, 5, 4]]


grafico = bx(lista)
grafico.mostrar_grafico()