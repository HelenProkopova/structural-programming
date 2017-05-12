import math

x = float(input("Введите x: "))
n = int(input("Введите n: "))

i = 1
s = 0

for i in range(i,n+1):
    if i % 2 != 0:
        s = s - (math.cos(i*x)/i**2)
    else:
        s = s + (math.cos(i*x)/i**2)
print(s)
