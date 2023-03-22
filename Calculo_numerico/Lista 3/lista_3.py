# Questão 1

n = 15

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
    if (x <= 2):
        soma, delta, n = 0, -1, 0
        while (abs(delta) > 0.00000000001):
            delta = exp(-1, n)
            delta *= fatorial(2*n)
            delta *= exp(x-1.0, n)
            delta /= (exp(fatorial(n), 2) * exp(4, n))
            soma += delta
            n += 1
        return soma
    else:
        return invsqrt(x/4) * 0.5

# Questão 3
def reverter (L):
    for i in range(0, (len(L)//2)):
        L[i] = L[-1-i] - L[i]
        L[-1-i] = L[-1-i] - L[i]
        L[i] = L[-1-i] + L[i]

def reversa (L):
    A = []
    for i in range(0, len(L)):
        A.append(L[i])
    reverter(A)
    return A


# Questão 4
def ordena(L):
    A = L[:]
    for i in range(1, len(A)):
        key_item = A[i]

        j = i - 1

        while j >= 0 and A[j] > key_item:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key_item
    return A



def Collatz(x0):
    return 2



def logaritmo_base2(x):
    pass

