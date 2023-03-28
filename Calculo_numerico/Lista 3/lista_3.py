# Questão 1

n = 15
n2_30 = 9.3132257e-11

def fatorial (x):
    produto = float(1)
    for i in range(1, x+1):
        produto *= i
    return produto

def exp(base, expoente):
    if (expoente >= 0):
        output = 1
        for i in range (0, expoente):
            output *= base
        return output
    else:
        return float(1/exp(base, expoente * (-1)))

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
def calcula_delta (x, n):
    if (n%2 == 0):
        i = 1.0
    else:
        i = -1.0
    fat = fatorial(n)
    return i * fatorial(2*n) * exp(x-1.0, n) / (fat*fat * exp(4, n))

def invsqrt(x):
    if (x <= 1.5):
        soma, delta, n = 0, float(1), 0
        while (abs(delta) > n2_30):
            delta = calcula_delta(x, n)
            soma += delta
            n+=1
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



# Questão 5
def logaritmo_base2(x):
    l0 = 1

    if (exp(2, l0) <= x):
        while (True):
            if (x < exp(2, l0+1)): break
            l0 += 1
    else:
        while (True):
            l0 -= 1
            if (exp(2, l0) <= x): break

    print(f" {exp(2, l0)} <= {x} < {exp(2, l0 + 1)}")

    
    

    return 












# Questão 6
def Collatz(x0):
    i = 0
    while True:
        if (x0 == 1): return i
        if (x0 % 2 == 0):
            x0 /= 2
        else:
            x0 = 3 * x0 + 1
        i += 1


x = 10
print(logaritmo_base2(x))

