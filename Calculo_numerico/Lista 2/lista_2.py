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

def Fin_gen_int(a, b, n):
    if (n == 0):
        return a
    elif (n == 1):
        return b
    else:
        return Fin_gen_int(a, b, n-1) + Fin_gen_int(a, b, n-2)









# Prints
print(f"Temperatura em Farenheit: {Celsius_para_Farenheit(32)}")
print(f"a é minúsculo? {minusculo('a')}")
print(f"A é minúsculo? {minusculo('A')}")
print(f"Transformando string em maiuscula: {frase_maiusculo('ola TUDO joia?')}")
a, b = 3, 2
print("Fibonacci:", Fin_gen_int(a, b, 0))
print("Fibonacci:", Fin_gen_int(a, b, 1))
print("Fibonacci:", Fin_gen_int(a, b, 2))
print("Fibonacci:", Fin_gen_int(a, b, 3))
print("Fibonacci:", Fin_gen_int(a, b, 4))