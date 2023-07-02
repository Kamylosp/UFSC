import numpy as np

elipses = np.load('teste_e.npy')

# Pontos conhecidos (x, y)
pontos = elipses[0]

# Montando as matrizes A e b
A = []
b = []

for x, y in pontos:
    row = [x**2, 2*x*y, y**2, 2*x, 2*y, 1]
    A.append(row)
    b.append(-1)  # Valor -F

# Resolvendo o sistema linear
coefficients = np.linalg.lstsq(A, b, rcond=None)[0]

# Coeficientes encontrados
A, B, C, D, E, F = coefficients

# Imprimindo os coeficientes
print("Coeficientes encontrados:")
print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)
print("E =", E)
print("F =", F)
