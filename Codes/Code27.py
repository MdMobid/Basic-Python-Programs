# Write A Program To Display Factorial of A Given Number

num=int(input("Enter A Number: "))
fact=num

for i in range (1,num+1):
  fact=fact*i
  
print("The Factorial of",num,"is:",fact)