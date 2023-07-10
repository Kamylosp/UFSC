def indice_maximo(L):
    max = L[0]
    ind = 0
    for i in range(0, len(L)):
        if (L[i] >= max):
            max = L[i]
            ind = i
    return ind