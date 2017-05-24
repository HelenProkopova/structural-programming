i = 1
j = 1
su = 1
arr = [[int(input()) for i in range(5)] for j in range(5)]

print("Введите элементы двумерного массива: ")

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i>j:
            su = su*arr[i][j]
print(su)
