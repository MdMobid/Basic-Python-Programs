# Write A Program To Take Input for a Number and check whether its a Part of Fibonacci Series (upto 80):

num=int(input("Enter a Number: "))
list1=[]
m=0
n=1
c=0

while n<89:
  a=m+n
  list1.append(m)
  m=n
  n=a

for i in range (0,len(list1)):
  if list1[i]==num:
    c=c+1
if c==1:
  print ("Found")
else:
    print("Not Found")
