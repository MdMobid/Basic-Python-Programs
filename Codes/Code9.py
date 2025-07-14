# Write A Program To Display Location and Frequency of a Given Element in List:

rng=int(input("How Many Numbers You Want to Operate? "))
list1=[]
print("Enter Your Numbers Below:")
for i in range (1,rng+1):
  num=int(input(">> "))
  list1.append(num)

print("")
count=0
loclst=[]
num=int(input("Enter The Element You Want To Check its Frequency: "))
for i in range (0,len(list1)):
  if num==list1[i]:
    count=count+1
    loclst.append(i)

print(">> Frequency:", count)
print(">> Locations:", loclst)