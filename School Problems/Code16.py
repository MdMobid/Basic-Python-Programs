# Write A Program To Display Binary Equivalent to a Given Decimal Number:

rem=0
list1=[]
n1=int(input("Enter A Number: "))
while n1>0:
  rem=n1%2
  n1=n1//2
  list1.append(rem)
print(list1[::-1])