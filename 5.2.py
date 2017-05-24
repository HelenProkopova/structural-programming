print("Введите массив: ")
a=[float(input()) for i in range(14)]
print('Исходный массив: ',a)
for i in range(7):
    a[i],a[i+7]=a[i+7],a[i]
print('Отсортированный массив: ',a)
