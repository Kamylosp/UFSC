# Vai reverter a lista enviada
def reverter (L):
    for i in range(0, (len(L)//2)):
        L[i], L[len(L)-1] = L[len(L)-1], L[i]

# Vai retornar uma lista reversa da recebida
def reversa (L):
    A = L[:]
    reverter(A)
    return A