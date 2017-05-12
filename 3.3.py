import math
y = 0
x = 0.1

while x<= 2.1:
    y = (x**2) - x*math.pi*math.cos(math.pi*x)
    print("При x = ",x," ответ = ",y)
    x = x + 0.2
