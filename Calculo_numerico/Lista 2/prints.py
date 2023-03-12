import lista_2 as l

# Prints

print(f"Temperatura em Farenheit: {l.Celsius_para_Farenheit(32)}")

print(f"a é minúsculo? {l.minusculo('a')}")
print(f"A é minúsculo? {l.minusculo('A')}")

print(f"Transformando string em maiuscula: {l.frase_maiusculo('ola TUDO joia?')}")

a, b = 3, 2
print("Fibonacci:", l.Fin_gen_int(a, b, 0))
print("Fibonacci:", l.Fin_gen_int(a, b, 1))
print("Fibonacci:", l.Fin_gen_int(a, b, 2))
print("Fibonacci:", l.Fin_gen_int(a, b, 3))
print("Fibonacci:", l.Fin_gen_int(a, b, 4))


fr = "L#6~=4~ziK4HEhO"
print("\nInput       :", fr)
print("Expected    : I#6~=4~wfH4EBeL")
print("Cifras Cesar:", l.cifra_cesar(23, fr))