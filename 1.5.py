import math

b = int(input("Введите b: "))
k = 3.4
y = 0
a = 0
t = 0

t = math.pow(b,2) + math.pow(k,3)
a = math.sqrt(b + t)
y = math.pow(math.sin(math.pow(a,2) + math.pow(b,2)),4)

print("t = ",t)
print("a = ",a)
print("y = ",y)
