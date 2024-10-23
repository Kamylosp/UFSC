import matplotlib.pyplot as plt
import numpy as np

def f_2B1Q_array_to_binary (binary_array, last_level=1):
    mapping =  {
        '00': 1,
        '01': 3,
        '10': -1,
        '11': -3
    }

    levels_array = []

    for i in range(0, len(binary_array), 2):

        # Pair of characters
        pair = binary_array[i:i+2]
        # Level of character
        level = mapping[pair]

        if last_level > 0:
            levels_array.append(level)
            last_level = level
        else:
            levels_array.append(-level)
            last_level = -level

    levels_array.append(levels_array[-1])

    return levels_array

def signals_to_plot(voltage_levels, symbol_duration=1):
    return np.arange(len(voltage_levels)), voltage_levels

def plot_2BQ1(time, sinal):
    
    plt.figure(figsize=(10, 6))
    plt.step(time, sinal, where='post')

    plt.xlim(-1, len(sinal)+1)
    plt.ylim(-4, 4)
    plt.yticks([-3, -1, 1, 3])

    plt.axhline(y=-3, color='gray', linestyle='--', linewidth=1)
    plt.axhline(y=-1, color='gray', linestyle='--', linewidth=1)
    plt.axhline(y=1, color='gray', linestyle='--', linewidth=1)
    plt.axhline(y=3, color='gray', linestyle='--', linewidth=1)

    for x in range(0, len(sinal), 1):
        plt.axvline(x=x, color='gray', linestyle='--', linewidth=0.5)

    plt.title('Codificação por 2BQ1')
    plt.xlabel('Tempo')
    plt.ylabel('Nível de tensão')

    plt.show()

def f_2B1Q_convert(string):
    binary_array = f_2B1Q_array_to_binary(string)

    arrays_to_plot = signals_to_plot(binary_array)

    plot_2BQ1(arrays_to_plot[0], arrays_to_plot[1])    