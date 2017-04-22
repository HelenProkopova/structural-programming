s = int(input("Введите стаж работы: "))
i = 3
k = 0
l = 0

if s == 0:
    k = 1
elif s > 0 and s < 2:
    k = 13
elif s >= 2 and s < 5:
    k = 16
    
for i in range(i,5):
    l = i * k
    if l>= 45:
        print("Принят в магистратуру при стаже ",s," и среднем балле ",i)
    
