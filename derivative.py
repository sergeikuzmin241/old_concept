# ПРОИЗВОДНЫЕ
print('ПРОИЗВОДНЫЕ')
import sympy as smp
from sympy import *
x, y = smp.symbols('x, y')
# Введу переменную К с различными индексами от 0 и до бесконечности, чтобы присвоить ей значение производной функции
# производная тригонометрической функции
print('производная тригонометрической функции')
k0 = smp.diff(((1 + smp.sin(x)) / (1 - smp.cos(x)))**2, x)
print(k0)
# производная логорифмической функции
print('производная логорифмической функции')
k1 = smp.diff(smp.log(x, 5)**(x/2), x)
print(k1)
# производная сложной функции
print('производная сложной функции')
print('Введем обозначения функций')
f, g = smp.symbols('f g', cls=smp.Function)
g = g(x)
f = f(x + g)
print(g)
print(f)
k2 = smp.diff(f, x)
print('Вычислим произвоную сложной функции', k2)