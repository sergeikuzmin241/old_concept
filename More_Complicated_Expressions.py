# Более сложные выражения
print('Более сложные выражения')
print('Интеграл №1')
import sympy as smp
from sympy import *
x, y = smp.symbols('x, y')
K = smp.integrate((1+smp.sqrt(x))**smp.Rational(1,3) / smp.sqrt(x), x)
print(K)
print('Интеграл №2')
Z = smp.integrate(x*(1-x**2)**smp.Rational(1/4), x)
print(Z)
print('Интеграл №3')
L = smp.integrate((2*x -1)*smp.cos(smp.sqrt(3*(2*x-1)**2 + 6)) / smp.sqrt(3*(2*x-1)**2 + 6), x)
print(L)