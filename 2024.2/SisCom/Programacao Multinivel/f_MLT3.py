import matplotlib.pyplot as plt
import numpy as np

def f_MLT3_array_to_binary(signal, last_level = -1, last_signed_level = -1):
    signal_output = []

    for i in signal:
        if i == '0':
            signal_output.append(last_level)

        else :
            if last_level == 1:
                signal_output.append(0)
                last_signed_level = 1
                last_level = 0

            elif last_level == -1:
                signal_output.append(0)
                last_signed_level = -1
                last_level = 0

            else:
                signal_output.append(-last_signed_level)
                last_level = -last_signed_level
    
    signal_output.append(signal_output[-1])
    
    return signal_output

def signals_to_plot(voltage_levels, symbol_duration=1):
    return np.arange(len(voltage_levels)), voltage_levels

def plot_MLT3(time, sinal):
    
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

    plt.title('Codificação por MLT3')
    plt.xlabel('Tempo')
    plt.ylabel('Nível de tensão')

    plt.show()


def f_MLT3_convert(string):
    binary_array = f_MLT3_array_to_binary(string)

    arrays_to_plot = signals_to_plot(binary_array)

    plot_MLT3(arrays_to_plot[0], arrays_to_plot[1]) 