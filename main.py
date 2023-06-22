# Оптимизация функции f(x) = (x - 3)**2
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from scipy.optimize import minimize

def f(x):
    return (x-3)**2
res = minimize(f, x0=2)
res.x
print(res.x)

# Оптимизация функции f(x,y) = (x - 1)**2 + (y - 2.5)**2

f = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2
cons = ({'type': 'ineq', 'fun': lambda x: x[0] - 2 * x[1] + 2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
bnds = ((0, None), (0, None))
res = minimize(f, (2, 0), bounds=bnds, constraints=cons)
res.x
print(res.x)

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

# 

x_data = np.linspace(0, 10, 10)
y_data = 3*x_data**2 + 2

plt.scatter(x_data, y_data)
plt.show()