# Write A Program To Display Factors of A Given Number

num=int(input("Enter A Positive Number: "))

print("\nThe Factors Of The Given Number Are As Follows: ")

for i in range (1,num+1):
  if num%i==0:
    print(i)