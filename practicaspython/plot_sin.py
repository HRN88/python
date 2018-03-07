#Graficar la funcion seno con python, se debe usar matplotlib

#https://matplotlib.org/api/pyplot_api.html hace uso de nump
import matplotlib.pyplot as plt

import numpy as np
import math

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html#numpy.arange
#numpy.arange Return evenly spaced values within a given interval.

#Genera un array de 0 a 1 con paso de 0.1
t = np.arange(0, 1, 0.01)

#Esto es similar a sin(2PiT) w = 2pi
s = np.sin(2 * np.pi * t)

#Con esto se crea la figura, y dentro un subplot
fig, ax = plt.subplots()

#Se grafica en ax
ax.plot(t, s)

#parametros para ax
ax.set(xlabel = 'time (s)', ylabel='voltage (mV)', title='Sin wave graph')

#regilla
ax.grid()

#visualizar la grafica
plt.show()

