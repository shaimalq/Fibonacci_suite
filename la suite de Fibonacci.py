n=int(input("saisir la valeur de n:"))
while n< 2:
    n=int(input("saisir la valeur de n:"))
upp= 0
up= 1
print("les termes de suite fibonacci sont:")
print(upp,end=" ")
print(up,end=" ")
for i in range (n-1):
    u= upp + up
    print(u, end=" ") 
    upp=up
    up=u   