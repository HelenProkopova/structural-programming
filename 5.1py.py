s=0
a=[int(input()) for i in range(17)]
for i in range(17):
    if a[i]%2!=0:
        s=s+a[i]
print(a)
for i in range(17):
    if a[i]%3==0:
        a[i]=s
print(a)
