import matplotlib.pyplot as plt
import numpy as np
from f_2BQ1 import f_2B1Q_convert
from f_MLT3 import f_MLT3_convert
from f_4DPAM5 import f_4DPAM5_convert
from f_8B6T import f_8B6T_convert

def string_to_binary(string):
    array = []

    for char in string:
        binary = format(ord(char), '08b')  
        array.append(binary)

    return ''.join(array)

print("Insira os caracteres (até 4) a serem codificados!")
string = input("caracteres: ")

binary_array = string_to_binary(string)

print("\n\nStrings converted to binary:")
print(binary_array, end='\n\n')

f_2B1Q_convert(binary_array)
f_MLT3_convert(binary_array)
f_4DPAM5_convert(binary_array)
f_8B6T_convert(binary_array)