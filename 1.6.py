import math

s1 = int(input("Введите площадь квадрата: "))
s2 = 0
r = 0
t = 0

r = math.sqrt(s1)/2
s2 = 2*r*r

print("Площадь вписанного квадрата = ",s2)

t = s1/s2

print("Меньше в ",t)
