import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from scipy import stats

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('Tempo (minutos)', fontsize=12)
ax.set_ylabel('Temperatura ($^\circ$C)', fontsize=12)
plt.title("Curva de Aquecimento")

x1 = np.arange(0.0, 8.5, 0.5)
y1 = np.array([60,61.2,64.8,66.3,68.7,70.1,71.2,72.8,74.3,
               75,76,76.5,76.9,77.2,77.8,78.1,78.7])

slope, intercept, r_value, p_value, std_err = stats.linregress(x1,y1)
plt.text(0,75, '$R^2$='+str(round(r_value**2,3)))

# Fit with polyfit
b, m = polyfit(x1, y1, 1)
plt.plot(x1, y1, 'bo')
plt.plot(x1, b + m * x1, '-')

x2 = np.arange(8.5, 15.0, 0.5)
y2 = np.array([79.1,79.3,79.3,79.3,79.5,79.5,79.8,79.8,80,
               80.1,80.1,80.3,80.4])

slope, intercept, r_value, p_value, std_err = stats.linregress(x2,y2)
plt.text(10,77, '$R^2$='+str(round(r_value**2,3)))

# Fit with polyfit
b, m = polyfit(x2, y2, 1)
plt.plot(x2, y2, 'go')
plt.plot(x2, b + m * x2, '-')

x3 = np.arange(15.0, 23.0, 0.5)
y3 = np.array([81,81.5,82.2,82.7,84,86,87.4,
              88,88,88,88,88,88.2,89,89.5,90.2])

slope, intercept, r_value, p_value, std_err = stats.linregress(x3,y3)
plt.text(18,83, '$R^2$='+str(round(r_value**2,3)))

# Fit with polyfit
b, m = polyfit(x3, y3, 1)
plt.plot(x3, y3, 'ro')
plt.plot(x3, b + m * x3, '-')


plt.show()