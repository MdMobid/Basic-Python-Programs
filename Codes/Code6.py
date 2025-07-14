# Write A Program To Display Sum of All The Numbers Present in a List

list1=[]
rng=int(input("How Many Numbers You Want to Operate? "))
print("Enter Your Numbers Below:")
for i in range (1,rng+1):
  num=int(input(">> "))
  list1.append(num)

sum=0
for j in range (0,len(list1)):
  sum=sum+list1[j]

print("Sum of All Numbers in The List is:", sum)