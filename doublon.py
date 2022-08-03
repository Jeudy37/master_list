n=[1,2,3,4,5,"je"]
n2=[3,4,2,"je"]
n3=[]
for i in n:
    if i not in n2:
        n3.append(i)
print(n3)        