n = int(input("Введите n: ")) 
m = int(input("Введите m: "))    
i = 1
j = 1
r = 1
s = 0
for i in range(n+1):
    for j in range(m):
        r = r*i
    s = s+r
    r = 1
print(s)
