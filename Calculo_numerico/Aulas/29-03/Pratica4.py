import numpy as np
0, 1, 2, 3
def mediana (L):
    L.sort()
    if (len(L)%2 == 0):
        out = (L[len(L)//2 - 1] + L[len(L)//2])/2
        return [out]
    else:
        return [L[len(L)//2]]

def medianas_linhas(A):
    x = np.empty((len(A), 1))
    for i in range(0, len(A)):
        x[i] = mediana(A[i])
    return x

L=[[-10.6486474 , -14.5256196 , -12.22596635 , -7.74696165] ,
[ 10.68030044 , 5.54195539 , 12.3896066 , 11.69923365]]

print(medianas_linhas(L))


L = []