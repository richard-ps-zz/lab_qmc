import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from scipy import stats

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('Tempo (minutos)', fontsize=12)
ax.set_ylabel('Temperatura ($^\circ$C)', fontsize=12)
plt.title("Curva de Resfriamento")

x1 = np.arange(0.0, 1.5, 0.5)
y1 = np.array([90,81,78.5])

slope, intercept, r_value, p_value, std_err = stats.linregress(x1,y1)
plt.text(0.6,85, '$R^2$='+str(round(r_value**2,3)))

# Fit with polyfit
b, m = polyfit(x1, y1, 1)
plt.plot(x1, y1, 'bo')
plt.plot(x1, b + m * x1, '-')

x1 = np.arange(1.5, 4.5, 0.5)
y1 = np.array([77.3,77,76.5,76,75.8,75])

slope, intercept, r_value, p_value, std_err = stats.linregress(x1,y1)
plt.text(2,73, '$R^2$='+str(round(r_value**2,3)))

# Fit with polyfit
b, m = polyfit(x1, y1, 1)
plt.plot(x1, y1, 'go')
plt.plot(x1, b + m * x1, '-')

x1 = np.arange(4.5, 9.0, 0.5)
y1 = np.array([74.3,73,71,69.5,67.5,65.5,63,62,59.5])

slope, intercept, r_value, p_value, std_err = stats.linregress(x1,y1)
plt.text(6,71, '$R^2$='+str(round(r_value**2,3)))

# Fit with polyfit
b, m = polyfit(x1, y1, 1)
plt.plot(x1, y1, 'ro')
plt.plot(x1, b + m * x1, '-')

plt.show()
