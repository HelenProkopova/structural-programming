a = float(input("Введите а: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if a > b and a > c:
    print(a,"больше")
elif b > a and b > c:
    print(b,"больше")
elif c > a and c > b:
    print(c,"больше")
