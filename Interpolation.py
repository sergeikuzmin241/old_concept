import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from scipy.optimize import minimize

# Предположим есть некотрые данные. Необходимо узнать значения между ними.

x = np.linspace(0, 10, 10)
print(x)
y = x**2 * np.sin(x)
plt.scatter(x,y)
plt.show()

from scipy.interpolate import interp1d

f = interp1d(x, y, kind='cubic')
x_dense = np.linspace(0, 10, 100)
y_dense = f(x_dense)
print(y_dense)
plt.plot(x_dense, y_dense)
plt.scatter(x, y)
plt.show()