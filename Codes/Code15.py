# Write A Program To Replace the Numbers present in a List by its Immediate Next Number:

a=[1,2,3,4,5,6,8,9,0]
b=[]

for j in range (1,len(a)):
  b.append(a[j])
a=b[::]
print(a)