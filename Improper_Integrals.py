# Неправильный интеграл
print('Неправильный интеграл')
print('Интеграл №1')
import sympy as smp
from sympy import *
x, y = smp.symbols('x, y')
K = smp.integrate(16*smp.atan(x) / (1+x**2), (x, 0, smp.oo))
print(K)