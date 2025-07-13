list1=[]
flist=[]
x=2
num=int(input("Enter A Number?: "))

for i in range (1,7):
    for j in range (1,7):
        m=i+j
        list1.append(m)

for k in range(2,13):
    y=list1.count(x)
    flist.append([x,y])
    x=x+1

for l in range (0,len(flist)):
  if num==int(flist[l][0]):
    indx=l
    findx=flist[l]

print("Probability of Getting", num,"is:", (findx[1]/36)*100, "%")
