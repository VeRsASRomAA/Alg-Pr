#Задача 1
N = int(input())
if N % 3 == 0:
    print("кратно")
else:
    print("не кратно")

#Задача 2 пункт 1
x = int(input())
y = int(input())
print("1) z =",(min(x,y) + 0.5)/(1+max(x,y)))
if x >=0:
    print("2) z =",max(x,y))
else: 
    print("2) z =",min(x,y))
if y >=0:
    print("3) z =",min(x,y))
else:
    print("3) z =",max(x2,y2))
#Задача 2 пункт 2
if x>=+0:
    print("2) z=", max)
else:
    print("2) z=", min)
if y>=0:
    print("3) z=", min)
else:
    if x**2 >= y**2:
        max=x
    else:
        min=y
    print("3) z=", max)
    
#Задача 3
x = int(input())
y = int(input())
z = int(input())
minXYZ = x
if x >=z:
    maxXZ = x
else:
    maxXZ = z
if y < minXYZ:
    minXYZ = y
if z < minXYZ:
    minXYZ = z
print("L =", 2*maxXZ - 3*minXYZ)
