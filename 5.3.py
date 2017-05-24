i = 1
j = 1
q = 1
mi = 10000000000000
su = 1
arr = [[int(input()) for i in range(3)] for j in range(3)]

print("Введите элементы двумерного массива: ")

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]<mi:
            mi=arr[i][j]
        if j==len(arr[i]):
            arr[i][1]=mi
            
print()             
                    
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()
