import math

x = float(input("Введите |x| < 1: "))
n = int(input("Введите n > 0: "))
i=1
s=0

if math.fabs(x) < 1 and n>0:
    for i in range(i,n+1):
        if i % 2 != 0:
            s = s + x*(i/i)
        else:
            s = s - x*(i/i)
print(s)
