import matplotlib.pyplot  as plt
import numpy as np



ejex=[i for i in range(30)] #crear numeros del 0 al 29
ejey=np.cos(ejex)
ejey2= -ejey

fig,axs = plt.subplots(1,2)
fig.suptitle("datos por separado")
axs[0].plot(ejex,ejey,'g-o',label="Funcion seno de un angulo")
axs[0].set_title("Funcion seno de un angulo")
axs[0].set_xlabel("eje x")
axs[0].set_ylabel("eje y")
axs[1].plot(ejex,ejey2,'r-x',label="Funcion seno de un angulo invertido")
axs[1].set_title("Funcion seno de un angulo invertido")
axs[1].set_xlabel("eje x")
axs[1].set_ylabel("eje y")
plt.show()