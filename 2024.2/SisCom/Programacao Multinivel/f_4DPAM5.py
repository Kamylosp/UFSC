import matplotlib.pyplot as plt
import numpy as np

def f_4DPAM5_array_to_binary (binary_array):
    mapping =  {
        '00': -2,
        '01': -1,
        '10': 1,
        '11': 2 }
    
    channel_1 = []
    channel_2 = []
    channel_3 = []
    channel_4 = []

    for i in range(0, len(binary_array), 8):
        channel_1.append(mapping[binary_array[i:i+2]])
        channel_2.append(mapping[binary_array[i+2:i+4]])
        channel_3.append(mapping[binary_array[i+4:i+6]])
        channel_4.append(mapping[binary_array[i+6:i+8]])
    
    channel_1.append(channel_1[-1])
    channel_2.append(channel_2[-1])
    channel_3.append(channel_3[-1])
    channel_4.append(channel_4[-1])

    return [channel_1, channel_2, channel_3, channel_4]

def signals_to_plot(voltage_levels, symbol_duration=1):
    return np.arange(len(voltage_levels[0])), voltage_levels

def plot_4DPAM5(time, signals):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    axs = axs.flatten()

    plt.suptitle('Codificação 4DPAM5 - Channels')

    for i in range(len(signals)):
        axs[i].step(time, signals[i], where='post')
        axs[i].set_ylim(-3, 3)  # Limites do eixo y
        
        axs[i].axhline(y=-2, color='gray', linestyle='--', linewidth=1)
        axs[i].axhline(y=-1, color='gray', linestyle='--', linewidth=1)
        axs[i].axhline(y=0, color='gray', linestyle='--', linewidth=1)
        axs[i].axhline(y=1, color='gray', linestyle='--', linewidth=1)
        axs[i].axhline(y=2, color='gray', linestyle='--', linewidth=1)
        
        for x in range(0, len(time)):
            axs[i].axvline(x=x, color='gray', linestyle='--', linewidth=0.5)  # Linha vertical

        axs[i].set_title(f'Channel {i+1}')
        axs[i].set_ylabel('Voltage')
        axs[i].set_yticks([-2, -1, 1, 2])

    plt.show()

def f_4DPAM5_convert(string):
    binary_arrays = f_4DPAM5_array_to_binary(string)

    arrays_to_plot = signals_to_plot(binary_arrays)

    plot_4DPAM5(arrays_to_plot[0], arrays_to_plot[1])    
