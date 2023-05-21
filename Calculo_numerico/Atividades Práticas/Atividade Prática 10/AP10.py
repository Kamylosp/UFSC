import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

def solve_determinante (A):
    '''Resolve o determinante por escalonamento
    
    Parâmetros obrigatórios
    ---------------------------
    A : Array-like de dimensao 2
        Matriz quadrada
    
    Saída
    ---------------------------
    det : float
          Determinante da matriz recebida
    '''
    n = len(A)

    # Escalonando a matriz
    for i in range(0, n):
        for j in range(i+1, n):
            coef = A[j, i]/A[i,i]
            
            A[j][:] -= coef * A[i][:]

    out = 1
    for i in range(n):
        out *= A[i, i]

    return out

n = 115

tabela = np.zeros((2, n + 2))

for i in range(1, n + 2):
    tabela[0, i] = i

for i in tqdm(range(2, n + 2)):

    aux = True
    while aux:
        try:
            A = (np.random.randint(-10, 10, (i,i))).astype(float)
            tempo_inicio = time.time()

            for j in range(10):
                _ = solve_determinante(A)  # Decomposição LU de $A$

            tempo_final = time.time()

            tabela[1, i] = (tempo_final - tempo_inicio) / 10
            aux = False

        except:
            pass


tabela = tabela.transpose()

m = tabela.shape[0]

dominio = np.linspace(0, n + 1, 1000)

# Define a matriz de coeficientes
A = np.zeros((m, 4))
for i in range(m):
    A[i, 0] = 1
    A[i, 1] = tabela[i, 0]
    A[i, 2] = tabela[i, 0] ** 2
    A[i, 3] = tabela[i, 0] ** 3

# Define o vetor independente
b = tabela[:, 1]
B = A.transpose() @ A
c = A.transpose() @ b

alpha = np.linalg.solve(B, c)

fig, axs = plt.subplots(1, 1, figsize=(6, 6))

axs.set_title("Tempo de criação das listas")
axs.set_xlabel("Tamanho da lista")
axs.set_ylabel("Tempo (s)")
tabela = tabela.transpose()
x, y = tabela[0, :], tabela[1, :]

axs.plot(x, y, 'ro',alpha=0.5, label="Testes")


plt.plot(x, y, 'ro')
im = [alpha[0] + alpha[1] * t + alpha[2] * t ** 2 +alpha[3] * t ** 3 for t in dominio]
plt.plot(dominio, im, 'b', label="Regressão cubica")

print()
print("-"*30)
print("Regressão Cúbica")
print("Coefs: ", alpha)

tabela = tabela.transpose()

A = np.zeros((m, 3))
for i in range(m):
    A[i, 0] = 1
    A[i, 1] = tabela[i, 0]
    A[i, 2] = tabela[i, 0] ** 2

# Define o vetor independente
b = tabela[:, 1]
B = A.transpose() @ A
c = A.transpose() @ b

alpha = np.linalg.solve(B, c)

im = [alpha[0] + alpha[1] * t + alpha[2] * t ** 2  for t in dominio]
plt.plot(dominio, im, 'g', label="Regressão quadrada")

print()
print("-"*30)
print("Regressão Quadrática")
print("Coefs: ", alpha)


A = np.zeros((m, 2))
for i in range(m):
    A[i, 0] = 1
    A[i, 1] = tabela[i, 0]

# Define o vetor independente
b = tabela[:, 1]
B = A.transpose() @ A
c = A.transpose() @ b

alpha = np.linalg.solve(B, c)

im = [alpha[0] + alpha[1] * t  for t in dominio]
plt.plot(dominio, im, 'y', label="Regressão linear")

print()
print("-"*30)
print("Regressão Linear")
print("Coefs: ", alpha)

plt.show()