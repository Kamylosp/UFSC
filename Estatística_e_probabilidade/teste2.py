import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

# make data:
np.random.seed(10)
D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))

# color
cor_barras = "#265fa6ff"

# plot
fig, ax = plt.subplots()
VP = ax.boxplot(D, positions=[2, 4, 6], widths=1.5, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": cor_barras, "edgecolor": "white",
                          "linewidth": 1.5},
                whiskerprops={"color": cor_barras, "linewidth": 1.5},
                capprops={"color": cor_barras, "linewidth": 1.5})

ax.set(xlim=(0, 8), ylim=(0,8))

#plt.xlim(0.5, 8)

fig.suptitle('test title', fontsize=12)

plt.xticks(np.arange(2, 8, step=2), ['January', 'February', 'March'])
plt.xlabel("Informação eixo X")


plt.show()
