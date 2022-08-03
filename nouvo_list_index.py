
#fe yon list ki pran tout eleman ki divizibl pa 3
#4
n=[1,2,3,"je",4,5,6,"m","j"]
n2=[]
for i in range(len(n)):
    if i % 3==0:
        n2.append(n[i])
print(n2)    