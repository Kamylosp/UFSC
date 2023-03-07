alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"

def Celcius_para_Farenheit(T):
    return T*1.8 + 32

def minusculo(c):
    if c in alfabeto_minusculo:
        return True
    return False

def frase_maiusculo(fr):
    string = ""
    for c in fr:
        if minusculo(c):
            c = chr(ord(c)-32)
        string += c
    return string

def Fib_gen_in(a,b,n):
    pass





# Prints
print(f"Temperatura em Farenheit: {Celcius_para_Farenheit(32)}")
print(f"a é minúsculo? {minusculo('a')}")
print(f"A é minúsculo? {minusculo('A')}")
print(f"Transformando string em maiuscula: {frase_maiusculo('ola TUDO joia?')}")