s=input ('введите строку: ')
t=int(0)
for i in range(len(s)):
    if s[i]== ',' or s[i]== '.' :
        t=t+1

print ('количество точек и запятых= ',t)         
    

