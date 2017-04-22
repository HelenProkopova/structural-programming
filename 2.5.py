z = 0
y = 0
x = 0

print("Z","Y","X","выражение")
for z in range(z,2):
    for y in range(y,2):
        for x in range(x,2):
          v = not(not x and y) or (x and not z)  
          print(z,y,x,v)
