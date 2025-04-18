# Отрезок [5,4 ; 5,6]
# Eps = 0,0001

from math import cos, sin

a = 8.0
b = 8.6
eps = 0.0001


def f(x):
    return (cos(x - 8) ** 2 - sin(x + 1)) / 2 - 0.2


k = 0  # количество итераций цикла
while b - a > 2 * eps:
    k += 1
    c = (a + b) / 2  # середина отрезка
    if f(a) * f(c) > 0:
        a = c
    else:
        b = c

x_vol = (a + b) / 2  # икс с волной
print("X с волной:", x_vol)
print("f(x_vol):", f(x_vol))
print("Кол-во итераций:", k)
