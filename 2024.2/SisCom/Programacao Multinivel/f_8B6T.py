import matplotlib.pyplot as plt
import numpy as np

def f_8B6T_adding (array_1, array2):
    array_to_return = []

    for i in array_1:
        array_to_return.append(int(i))

    for i in array2:
        array_to_return.append(int(i))

    return array_to_return

def f_8B6T_array_to_binary(signal, ultimo_peso=-1):

    array_elements = np.load('valores_8B6T.npy') 

    signal_output = []

    for i in range(0, len(signal), 8):

        index = int(signal[i:i+8], 2)

        if sum(array_elements[index]) > 0:
            if ultimo_peso > 0:
                signal_output = f_8B6T_adding (signal_output, -1*array_elements[index])
                ultimo_peso = -1

            else:
                signal_output = f_8B6T_adding (signal_output, array_elements[index])
                ultimo_peso = +1

        elif sum(array_elements[index]) < 0:
            if ultimo_peso > 0:
                signal_output = f_8B6T_adding (signal_output, array_elements[index])
                ultimo_peso = -1
            else:
                signal_output = f_8B6T_adding (signal_output, -1*array_elements[index])
                ultimo_peso = +1

        else:
            signal_output = f_8B6T_adding (signal_output, array_elements[index])
    
    signal_output.append(signal_output[-1])
    
    return signal_output

def signals_to_plot(voltage_levels, symbol_duration=1):
    return np.arange(len(voltage_levels)), voltage_levels

def plot_8B6T(time, sinal):
    
    plt.figure(figsize=(10, 6))
    plt.step(time, sinal, where='post')

    plt.xlim(-1, len(sinal)+1)
    plt.ylim(-2, 2)
    plt.yticks([ -1, 0, 1])

    plt.axhline(y=-1, color='gray', linestyle='--', linewidth=1)
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=1)
    plt.axhline(y=1, color='gray', linestyle='--', linewidth=1)

    for x in range(0, len(sinal), 1):
        plt.axvline(x=x, color='gray', linestyle='--', linewidth=0.5)

    plt.title('Codificação por 8B6T')
    plt.xlabel('Tempo')
    plt.ylabel('Nível de tensão')

    plt.show()


def f_8B6T_convert(string):
    binary_array = f_8B6T_array_to_binary(string)

    arrays_to_plot = signals_to_plot(binary_array)

    plot_8B6T(arrays_to_plot[0], arrays_to_plot[1]) 