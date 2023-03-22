# Questão 1

n = 15
n2_30 = 9.3132257e-10


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

# Questão 2
def invsqrt(x):
    soma, delta, n = 0, -1, 0
    while (abs(delta) > n2_30):
        delta = exp(-1, n)*fatorial(2*n)*exp(x-1, n)/(exp(fatorial(n), 2) * exp(4, n))
        soma += delta
    return soma



# Questão 3
def reverter (L):
    for i in range(0, (len(L)//2)):
        L[i] = L[-1-i] - L[i]
        L[-1-i] = L[-1-i] - L[i]
        L[i] = L[-1-i] + L[i]

def reversa (L):
    A = L[:]
    reverter(A)
    return A


# Questão 4
def ordena(L):
    for i in range(1, len(L)):
        key_item = L[i]

        j = i - 1

        while j >= 0 and L[j] > key_item:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key_item
    return L


