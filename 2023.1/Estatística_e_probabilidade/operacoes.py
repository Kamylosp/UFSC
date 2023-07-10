import statistics

def media (lista):
    return statistics.mean(lista)

def mediana (lista):
    return statistics.median(lista)

def media_harmonica (lista):
    return statistics.harmonic_mean(lista)

def moda (lista):
    return statistics.mode(lista)

def variancia (lista):
    return statistics.variance(lista)

def desvio_padrao_amostra (lista):
    return statistics.stdev(lista)

def desvio_padrao_populacional (lista):
    return statistics.pstdev(lista)

def primeiro_quartil (lista):
    return statistics.median_low(lista)

def terceiro_quartil (lista):
    return statistics.median_high(lista)






def printa_informacoes (lista):
    print(f"Media: {media(lista):.3f}")
    print(f"Mediana: {mediana(lista):.3f}")
    print(f"1º Quartil: {primeiro_quartil(lista):.3f}")
    print(f"3º Quartil: {terceiro_quartil(lista):.3f}")
    print(f"Variancia: {variancia(lista):.3f}")
    print(f"Desvio Padrao: {desvio_padrao_amostra(lista):.3f}")
    print(f"Moda: {moda(lista):.3f}")
    print(f"Média Harmônica: {media_harmonica(lista):.3f}")