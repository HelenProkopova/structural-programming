import math

s = 0
x = float(input("Введите x: "))
y = float(input("Введите y: "))

if math.fabs(x)>0.5 and y>0.5 and math.fabs(x)==y:
    print("Точка не входит в закрашенную область")   
else:
    print("Точка входит в закрашенную область")

    
        
