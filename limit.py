# ПРЕДЕЛЫ ФУНКЦИЙ
print('ПРЕДЕЛЫ ФУНКЦИЙ')
import sympy as smp
from sympy import *
# Введу переменную К с различными индексами от 0 и до бесконечности, чтобы присвоить ей значение предела функции 
print('Введу переменную К с различными индексами от 0 и до бесконечности, чтобы присвоить ей значение предела функции')
x, y = smp.symbols('x, y')
# Предел функции при x стремится к pi
print('Предел функции при x стремится к pi')
k0 = smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi)
print(k0)
# Предел функции при x стремится к 0 справа
print('Предел функции при x стремится к 0 справа')
k1 = smp.limit(2*smp.exp(1/x) / (smp.exp(1/x)+1), x, 0, dir='+')
print(k1)
# Предел функции при x стремится к 0 слева
print('Предел функции при x стремится к 0 слева')
k2 = smp.limit(2*smp.exp(1/x) / (smp.exp(1/x)+1), x, 0, dir='-')
print(k2)
# # Предел функции при x стремится к бесконечности
print('Предел функции при x стремится к бесконечности')
k3 = smp.limit((smp.cos(x) -1)/x, x, smp.oo)
print(k3)