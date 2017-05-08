import math

y = int(input("Введите y: "))
x = int(input("Введите x: "))
R = 0

R = math.fabs(math.sqrt(math.pow(math.sin(y),2)+6.835)+ math.exp(x))

print("R = ",R)
