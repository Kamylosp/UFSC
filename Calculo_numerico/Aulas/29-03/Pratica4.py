import numpy as np

def medianas_linhas(A):
    x = np.empty((len(A), 1))
    for i in range(0, len(A)):
        # A[i].sort()
        x[i] = np.median(A[i])
    return x

L=[[-10.6486474 , -14.5256196 , -12.22596635 , -7.74696165] ,
[ 10.68030044 , 5.54195539 , 12.3896066 , 11.69923365]]

print(medianas_linhas(L))


L = []