# Write A Program To Display Frequency of Each Number Present In a List:

a=[1,2,3,4,5,5,4,3,2,1,0,1,1]
b=[]

for i in a:
  if i not in b:
    b.append(i)

countlist=[]
for i in range (0,len(a)):
  count=a.count(a[i])
  countlist.append(count)

for k in range (0,len(b)):
  print(b[k], ">>", countlist[k])
