alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"

def Celsius_para_Farenheit(T):
    return (T*1.8 + 32)

def minusculo(c):
    if c in alfabeto_minusculo:
        return True
    return False

def muda_maiusculo(c):
    if minusculo(c):
        return chr(ord(c)-32)
    return c

def frase_maiusculo(fr):
    if (len(fr) > 1):
        return muda_maiusculo(fr[0]) + frase_maiusculo(fr[1:])
    else:
        return muda_maiusculo(fr[0])

def Fib_gen_in(a, b, n):
    if (n == 0):
        return a
    elif (n == 1):
        return b
    else:
        return Fib_gen_in(a, b, n-1) + Fib_gen_in(a, b, n-2)

def Fin_gen_int(a, b, n):
    if (n == 0):
        return a
    elif (n == 1):
        return b
    else:
        return Fin_gen_int(a, b, n-1) + Fin_gen_int(a, b, n-2)














def muda_cifra_cesar(n, c):
    if (97 <= ord(c) <= 122) or (65 <= ord(c) <= 90):
        letra = ord(c) + n
        if (ord(c) <= 122 and letra > 122) or (ord(c) <= 90 and letra > 90):
            letra -= 26
        return chr(letra)
    else:
        return c


def cifra_cesar (n, fr):
    if (len(fr) > 1):
        return muda_cifra_cesar(n, fr[0]) + cifra_cesar(n, fr[1:])
    else:
        return muda_cifra_cesar(n, fr[0])