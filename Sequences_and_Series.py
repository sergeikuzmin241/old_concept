# Последовательности и серии
print('Последовательности и серии')
import sympy as smp
from sympy import *
n = smp.symbols('n')
N = smp.Sum(6/4**n, (n, 0, smp.oo)).doit()
print(N)
Z = smp.Sum(2**(n+1) / 5**n, (n, 0, smp.oo)).doit()
print(Z)