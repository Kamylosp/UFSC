import numpy as np

def medianas_linhas(A):
    x = np.empty((len(A), 1))
    for i in range(0, len(A)):
        # A[i].sort()
        x[i] = np.median(A[i])
    return x