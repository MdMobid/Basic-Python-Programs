# Write A Program To Display Fibonacci Series:

nterms=int(input("How Many Terms Do You want in your Fibonacci Series? "))
list1=[]
n1=0
n2=1
count=0

while count<nterms:
  list1.append(n1)
  a=n1+n2
  n1=n2
  n2=a
  count=count+1
print(list1)