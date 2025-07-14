# Write A Program To Display Highest Number Present in a List:

rng=int(input("How Many Numbers You Want to Operate? "))
list1=[]
print("Enter Your Numbers Below:")
for i in range (1,rng+1):
  num=int(input(">> "))
  list1.append(num)

print("")
max=list1[0]
for i in range (1,len(list1)):
  if max<list1[i]:
    max=list1[i]

print("The Highest Number in the List is:", max)