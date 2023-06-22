# Практика
print('Практика')
import sympy as smp
from sympy import *
# Дано dy/dx = 8x + csc^2(x) c y(pi/2) = -7 найти решение для y(x)
print('Дано dy/dx = 8x + csc^2(x) c y(pi/2) = -7 найти решение для y(x)')
x, y = smp.symbols('x, y')
integral = smp.integrate(8*x + smp.csc(x)**2, x)
C = integral.subs(x, smp.pi/2) - 7
y = integral + C
z = y.subs(x, smp.pi/2)
print(integral)
print(C)
print(y)
print(z)