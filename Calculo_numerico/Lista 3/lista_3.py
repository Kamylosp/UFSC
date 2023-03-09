# Questão 1

n = 11
base = 9.3132257e-10

def fatorial (x):
    if (x <= 1):  
        return 1
    else:       
        return x*fatorial(x-1)

def exp(base, expoente):
    output = 1
    for i in range (0, expoente):
        output *= base
    return output

def sin (x):
    soma = 0
    for i in range (n):
        soma += (1 - 2*(i%2))/(fatorial(2*i+1)) * (exp(x, 2*i+1))
    return soma

def cos (x):
    soma = 0
    for i in range (n):
        soma += (1 - 2*(i%2))/(fatorial(2*i)) * (exp(x, 2*i))
    return soma
        

# Vai reverter a lista enviada
def reverter (L):
    for i in range(0, (len(L)//2)):
        L[i], L[len(L)-1] = L[len(L)-1], L[i]

# Vai retornar uma lista reversa da recebida
def reversa (L):
    A = L[:]
    reverter(A)
    return A