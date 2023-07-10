alfabeto = "abcdefghijklmnopqrstuvwxyz"

entrada = input("Digite uma string: ")

numero_minusculas = 0

for i in entrada:
    if i in alfabeto:
        numero_minusculas+=1

print("Numero de minusculas: ", numero_minusculas)