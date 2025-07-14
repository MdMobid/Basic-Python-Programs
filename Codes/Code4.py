# Write A Program To Take Input for a Number and check whether its a Part of Fibonacci Series (upto 80)

num=int(input("Enter a Number: "))
nterms=20
list1=[]
n1=0
n2=1
count=0
c=0

while count<nterms:
  a=n1+n2
  list1.append(n1)
  n1=n2
  n2=a
  count+=1

for i in range (0,len(list1)):
  if list1[i]==num:
    c=c+1
if c==1:
  print ("Found")
else:
    print("Not Found")