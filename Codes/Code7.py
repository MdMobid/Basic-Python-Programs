# Write A Program To Display Each Alternate Numbers in a List:

rng=int(input("How Many Numbers You Want to Operate? "))
list1=[]
print("Enter Your Numbers Below:")
for i in range (1,rng+1):
  num=int(input(">> "))
  list1.append(num)

print("")
for i in range (0,len(list1),2):
  print(list1[i])