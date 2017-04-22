import math

a = float(input("Введите a: "))
b = float(input("Ведите b: "))

z = (a**2)-(2*a*b)+(b**2)
s = math.fabs((a**2)-(2*a*b)+(b**2))

if z > s:
    print("Квадрат разности больше")
elif z == s:
    print("Равны")
else:
    print("Модуль квадрата разности больше")
