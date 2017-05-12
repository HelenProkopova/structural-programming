m = int(input("Введите m: "))    
i = 100
r = 0
for i in range(i,1001,100):
    if (i/100)%2!=0:
        r = i/m
        print(r)
    r = 0
