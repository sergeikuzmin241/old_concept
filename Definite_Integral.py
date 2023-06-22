# Определенный интеграл
print('Определенный интеграл')
print('Интеграл №1')
import sympy as smp
from sympy import *
x, y = smp.symbols('x, y')
print('Вычеслим определенный интеграл, где пределами интегрирования являются 0 и log(4)')
K = smp.integrate(smp.exp(x) / smp.sqrt(smp.exp(2*x) + 9), (x, 0, smp.log(4)))
print(K)
print('Интеграл №2')
print('Вычеслим определенный интеграл, где пределами интегрирования являются 1 и t')
print('Введём переменную t')
t = smp.symbols('t')
Z = smp.integrate(x**10*smp.exp(x), (x, 1, t))
print(Z)
