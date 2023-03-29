import numpy as np
import matplotlib.pyplot as plt

class boxplot():

    def __init__(self, lista, estilo = 'bmh', cor = "#265fa6ff"):
        plt.style.use(estilo)
        self.cor_barras = cor
        self.fig, self.ax = plt.subplots()

        self.qtdd_colunas = len(lista)

        self.VP = self.ax.boxplot(lista, positions=np.arange(2, 2*self.qtdd_colunas + 2, step=2), widths=1.5, patch_artist=True,
                     showmeans=False, showfliers=True,
                        medianprops={"color": "white", "linewidth": 0.5},
                        boxprops={"facecolor": self.cor_barras, "edgecolor": "white",
                                "linewidth": 0.5},
                        whiskerprops={"color": self.cor_barras, "linewidth": 1.5},
                        capprops={"color": self.cor_barras, "linewidth": 1.5})

        # self.ax.set(xlim=(70,260))
        self.ax.set(ylim=(40,260))

    def nome_das_barras (self, lista_nomes):
        plt.xticks(np.arange(2, 2*self.qtdd_colunas + 2, step=2), lista_nomes)
    
    def titulo (self, texto, fonte = 12):
        self.fig.suptitle(texto, fontsize=fonte)
    
    def legenda_eixo_x (self, texto, fonte=12):
        plt.xlabel(texto, fontsize=fonte)

    def legenda_eixo_y (self, texto, fonte=12):
        plt.ylabel(texto, fontsize=fonte)

    

    def mostrar_grafico(self):
        plt.show()