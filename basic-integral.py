# Основы интегрирования
print('Основы интегрирования')
import sympy as smp
from sympy import *
# Интегралы от тригонометрической функции
x, y = smp.symbols('x, y')
print('Интегралы от тригонометрической функции')
k0 = smp.integrate(smp.csc(x)*smp.cot(x), x)
print(k0)
k1 = smp.integrate(4*smp.sec(3*x)*smp.tan(3*x), x)
print(k1)
k2 = smp.integrate(2/smp.sqrt(1-x**2) - 1/x**smp.Rational(1,4), x)
print(k2)